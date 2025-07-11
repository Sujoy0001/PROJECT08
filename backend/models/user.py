from pydantic import BaseModel, EmailStr
from typing import Literal, Optional

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None
    profile_img: Optional[str] = None  # URL or base64
    password: str
    role: Literal['user']
    
class LoginUser(BaseModel):
    email: EmailStr
    password: str


class Technician(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None
    password: str
    role: Literal['technician']