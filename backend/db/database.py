from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["FTech"]
users_collection = db["users"]
technicians_collection = db["technicians"]
technician_profiles_collection = db["technician_profiles"]
technician_profiles_reviews_collection = db["reviews"]
