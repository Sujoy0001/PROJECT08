from fastapi import APIRouter, Query
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
