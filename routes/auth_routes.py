from fastapi import APIRouter, Form, HTTPException
import constants

router = APIRouter()

@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "123":
        return {
            "access_token": constants.FAKE_VALID_TOKEN,
            "token_type": "bearer"
        }
    raise HTTPException(
        status_code = 401,
        detail = constants.INVALID_EXPIRED_TOKEN
    )
