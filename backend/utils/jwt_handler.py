from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "fd43ae0cd9b6d15f6f290cf812e90ef041d7ef3c2f195c5e2a8d93db4846c778"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
