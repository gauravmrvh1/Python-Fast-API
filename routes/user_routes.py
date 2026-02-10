from fastapi import APIRouter, Form, Depends
import schemas
from sqlalchemy.orm import Session
import auth, models, database

router = APIRouter()

@router.post("/users_list")
def get_users(db: Session = Depends(database.get_db), token: str = Depends(auth.get_current_token)):
    auth.verify_token(token)
    return db.query(models.User).limit(1000).all()

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
        "age": 2
    }

@router.post("/users1")
async def create_users(user: schemas.User):
    return user