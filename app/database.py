from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "ecomm_db")

client = AsyncIOMotorClient(
    MONGO_URL,
    serverSelectionTimeoutMS=30000,
)
db = client[DB_NAME]

users_collection = db["users"]
products_collection = db["products"]