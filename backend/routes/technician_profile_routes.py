from fastapi import APIRouter, HTTPException
from models.technician_profile import TechnicianProfile
from db.database import technician_profiles_collection, technicians_collection  # add this!

router = APIRouter()

@router.post("/technician/profile")
async def create_technician_profile(profile: TechnicianProfile):
    # ✅ 1. Check if technician exists (must register first)
    technician = await technicians_collection.find_one({"id": profile.technician_id})
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not registered")

    # ✅ 2. Check if profile already exists
    existing_profile = await technician_profiles_collection.find_one({"technician_id": profile.technician_id})
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already completed")

    # ✅ 3. Insert new profile
    await technician_profiles_collection.insert_one(profile.dict())
    return {"message": "Technician profile created successfully"}
