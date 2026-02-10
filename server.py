from fastapi import FastAPI, Form, HTTPException, Depends
from schemas import User as UserSchema
from models import User as UserModel
import auth
from sqlalchemy.orm import Session
from database import get_db
from routes import auth_routes, base_routes

app = FastAPI()
app.include_router(auth_routes.router)
app.include_router(base_routes.router)


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
async def search(q: str, page: int = 1):
    return {"query": q, "page": page}

@app.post("/users1")
async def create_users(user: UserSchema):
    return user

@app.post("/users")
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

@app.get("/dashboard")
async def dashboard(token: str = Depends(auth.get_current_token)):
    auth.verify_token(token)
    return {
        "success": "true"
    }

@app.get("/users_list")
def get_users(db: Session = Depends(get_db), token: str = Depends(auth.get_current_token)):
    auth.verify_token(token)
    return db.query(UserModel).limit(1000).all()