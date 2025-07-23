from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/spendy")
client = AsyncIOMotorClient(MONGODB_URL)
db = client["spendy"]