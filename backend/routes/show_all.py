from fastapi import APIRouter, Query, HTTPException
from db.database import technician_profiles_collection, technicians_collection

router = APIRouter()

@router.get("/technicians/search")
async def search_technicians(
    area: str = Query(..., description="Area where technician works"),
    category: str = Query(..., description="Service category")
):
    query = {
        "work_areas": area,
        "service_category": category
    }

    results = []
    async for profile in technician_profiles_collection.find(query):
        # Fetch technician basic data
        technician = await technicians_collection.find_one({"id": profile["technician_id"]})
        
        # If technician exists, merge full_name and username
        profile_data = {
            "_id": str(profile["_id"]),
            "technician_id": profile["technician_id"],
            "service_category": profile["service_category"],
            "experience_years": profile["experience_years"],
            "work_areas": profile["work_areas"],
            "phone_or_whatsapp": profile["phone_or_whatsapp"],
            "about": profile["about"],
            "profile_image": profile.get("profile_image"),
            "age": profile["age"],
            "gender": profile["gender"],
            "qualifications": profile.get("qualifications", ""),
            "full_name": technician["full_name"] if technician else "",
            "username": technician["username"] if technician else ""
        }

        results.append(profile_data)

    if not results:
        return {"message": "No technicians found for the specified area and category."}

    return {"results": results}


# Get technician profile by technician ID
@router.get("/technicians/{technician_id}")
async def get_technician_profile(technician_id: int):
    technician = await technicians_collection.find_one({"id": technician_id})
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not found")

    profile = await technician_profiles_collection.find_one({"technician_id": technician_id})
    if not profile:
        raise HTTPException(status_code=404, detail="Technician profile not found")
    
    # Combine technician basic data and profile data
    profile_data = {
        "technician_id": technician_id,
        "full_name": technician.get("full_name", ""),
        "username": technician.get("username", ""),
        "profile_image": profile.get("profile_image"),
        "service_category": profile.get("service_category"),
        "experience_years": profile.get("experience_years"),
        "work_areas": profile.get("work_areas"),
        "phone_or_whatsapp": profile.get("phone_or_whatsapp"),
        "about": profile.get("about"),
        "age": profile.get("age"),
        "gender": profile.get("gender"),
        "qualifications": profile.get("qualifications", "")
    }

    return profile_data