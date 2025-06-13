from fastapi import APIRouter
from app.db.mongo import db
from app.models.user import User

router = APIRouter()

@router.get("/test-mongo")
async def test_mongo():
    doc = await db["documents"].find_one()
    return {"document": doc}

@router.get("/test")
async def test_connection():
    collections = await db.list_collection_names()
    return {"collections": collections}

@router.post("/add_user")
async def add_user(user: User):
    result = await db["users"].insert_one(user.dict())
    return {"inserted_id": str(result.inserted_id)}

@router.get("/users")
async def get_users():
    users = []
    async for user in db["users"].find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users
