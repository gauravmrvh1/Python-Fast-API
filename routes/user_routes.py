from fastapi import APIRouter, Form
import schemas

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.post("/")
async def create_user(
    name: str = Form(...),
    email: str = Form(...),
    age: int = Form(...)
):
    return {
        "name": name,
        "email": email,
        "age": age
    }

@router.post("/users1")
async def create_users(user: schemas.User):
    return user