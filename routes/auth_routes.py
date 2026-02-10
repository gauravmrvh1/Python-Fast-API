from fastapi import APIRouter, Form, HTTPException, Depends
import Config.constants as constants
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import Config.jwt_config as jwt_config
from jose import jwt
import Services.auth as authService

router = APIRouter()

@router.post("/login")
def login(
    # username: str = Form(...),
    # password: str = Form(...)
    form: OAuth2PasswordRequestForm = Depends()
):
    try:
        if form.username == "admin" and form.password == "123":
            return {
                "access_token": constants.FAKE_VALID_TOKEN,
                "token_type": "bearer"
            }
        else:
            access_token = authService.create_access_token(
                data={"sub": form.username},
                expires_delta=timedelta(minutes=jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES)
            )
            refresh_token = authService.create_refresh_token(
                data={"sub": form.username},
            )
            
            opaqueToken = authService.generate_token()
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "opaqueToken": opaqueToken,
                "token_type": "bearer"
            }
            
    except Exception as e:
        raise HTTPException(
            status_code = 401,
            detail = constants.INVALID_EXPIRED_TOKEN
        )

@router.post("/refresh")
def refresh_token(refresh_token: str):
    payload = jwt.decode(refresh_token, jwt_config.SECRET_KEY, algorithms=[jwt_config.ALGORITHM])
    new_access = authService.create_access_token(
        {"sub": payload["sub"]},
        timedelta(minutes=30)
    )
    return {"access_token": new_access}

@router.get("/profile")
def profile(user=Depends(authService.get_current_user)):
    return {"user": user}