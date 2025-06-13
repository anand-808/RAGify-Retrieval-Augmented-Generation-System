from fastapi import APIRouter
from app.db.mongo import db

router = APIRouter()

@router.get("/test-mongo")
async def test_mongo():
    doc = await db["documents"].find_one()
    return {"document": doc}

@router.get("/test")
async def test_connection():
    collections = await db.list_collection_names()
    return {"collections": collections}