from fastapi import APIRouter, HTTPException
from models.user import User, LoginUser as LoginData, Technician
from db.database import users_collection, technicians_collection
from utils.hash_password import hash_password, verify_password
from utils.jwt_handler import create_access_token

router = APIRouter()

# Get the next user ID (auto-increment)
async def get_next_user_id():
    last_user = await users_collection.find_one(sort=[("id", -1)])
    return last_user["id"] + 1 if last_user else 1

async def get_next_technician_id():
    last_technician = await technicians_collection.find_one(sort=[("id", -1)])
    return last_technician["id"] + 1 if last_technician else 1

@router.post("/register")
async def register(user: User):
    if await users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    if await users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    user_dict = user.dict()
    user_dict["id"] = await get_next_user_id()
    user_dict["password"] = hash_password(user.password)
    

    await users_collection.insert_one(user_dict)
    return {"message": "User registered successfully", "id": user_dict["id"]}


@router.post("/register/technicians")
async def register_technician(technician: Technician):
    if await technicians_collection.find_one({"email": technician.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    technician_dict = technician.dict()
    technician_dict["id"] = await get_next_technician_id()
    technician_dict["password"] = hash_password(technician.password)

    await technicians_collection.insert_one(technician_dict)
    return {"message": "technicians registered successfully", "id": technician_dict["id"]}

@router.post("/login")
async def login(email: str, password: str):
    user = await technicians_collection.find_one({"email": email})
    role = "technician"

    if not user:
        user = await users_collection.find_one({"email": email})
        role = "user"

    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")

    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "role": role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": role
    }
