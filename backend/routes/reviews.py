from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from db.database import technician_profiles_reviews_collection, technicians_collection, users_collection
from models.reviews import reviews

router = APIRouter()
@router.post("/technician/review/{technician_id}")
async def post_review(review: reviews, technician_id: int, user_id: int):
    user = await users_collection.find_one({"id": user_id})
    
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    technician = await technicians_collection.find_one({"id": technician_id})
    
    if not technician:
        raise HTTPException(status_code=404, detail="technician not found")

        
    await technician_profiles_reviews_collection.insert_one(review.dict())
    return {"message": "review submit successfully"}