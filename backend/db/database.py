from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["FTech"]
users_collection = db["users"]
technicians_collection = db["technicians"]
