from pydantic import BaseModel
from typing import List, Optional, Literal

class TechnicianProfile(BaseModel):
    
     
    technician_id: int  # foreign key to the technician
    service_category: Literal[
        "Electrician", "Plumber", "AC Repair", "Carpenter", 
        "Painter", "Technician", "Mobile Repair", 
        "CCTV", "Computer Repair", "Other"
    ]
    experience_years: int
    work_areas: List[str]
    phone_or_whatsapp: int
    about: str
    profile_image: Optional[str]  # URL or base64
    age: int
    gender: Literal['male', 'female', 'other']
    qualifications: Optional[str]
