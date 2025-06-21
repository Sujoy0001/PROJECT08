from fastapi import APIRouter, HTTPException
from models.user import User, LoginUser as LoginData
from db.database import users_collection
from utils.hash_password import hash_password, verify_password
from utils.jwt_handler import create_access_token

router = APIRouter()

# Get the next user ID (auto-increment)
async def get_next_user_id():
    last_user = await users_collection.find_one(sort=[("id", -1)])
    return last_user["id"] + 1 if last_user else 1

@router.post("/register")
async def register(user: User):
    if await users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    if await users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    user_dict = user.dict()
    user_dict["id"] = await get_next_user_id()
    user_dict["password"] = hash_password(user.password)
    
    if user.role not in ["user", "technician"]:
        raise HTTPException(status_code=400, detail="Invalid role specified")

    await users_collection.insert_one(user_dict)
    return {"message": "User registered successfully", "id": user_dict["id"]}


@router.post("/login")
async def login(login_data: LoginData):
    user = await users_collection.find_one({"email": login_data.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(login_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    token_data = {
        "sub": user["email"],
        "id": user["id"],
        "username": user["username"],
        "full_name": user["full_name"]
    }

    token = create_access_token(token_data)
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "full_name": user["full_name"],
            "email": user["email"]
        }
    }
