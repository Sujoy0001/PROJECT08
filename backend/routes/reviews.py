from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from db.database import technician_profiles_reviews_collection, technicians_collection, users_collection
from models.reviews import reviews

router = APIRouter()

@router.post("/technician/review/{technician_id}")
async def post_review(review: reviews, technician_id: int, user_id: int):
    # Find user by id
    user = await users_collection.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    # Find technician by id
    technician = await technicians_collection.find_one({"id": technician_id})
    if not technician:
        raise HTTPException(status_code=404, detail="technician not found")

    # Add user details and technician_id into review
    review_data = review.dict()
    review_data["user_full_name"] = user.get("full_name")
    review_data["user_profile_img"] = user.get("profile_img")
    review_data["technician_id"] = technician_id

    # Insert review
    await technician_profiles_reviews_collection.insert_one(review_data)
    
    return {"message": "review submitted successfully"}


@router.get("/technician/{technician_id}/reviews")
async def get_reviews_for_technician(technician_id: int):
    reviews_cursor = technician_profiles_reviews_collection.find({"technician_id": technician_id})
    reviews_list = []
    async for review in reviews_cursor:
        review["_id"] = str(review["_id"])  # Convert ObjectId to string for JSON serializable
        reviews_list.append(review)
        
    if not reviews_list:
        raise HTTPException(status_code=404, detail="No reviews found for this technician")
    else:
        return {"reviews": reviews_list}

