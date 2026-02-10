from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import Config.constants as constants
from jose import jwt, JWTError
from Config.jwt_config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_token(token: str = Depends(oauth2_scheme)) -> str:
    if token != constants.FAKE_VALID_TOKEN:
        return token
    else:
        raise HTTPException(
            status_code = 401,
            detail = constants.INVALID_EXPIRED_TOKEN
        )

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def verify_token(token: str) -> str | HTTPException:
    if token != constants.FAKE_VALID_TOKEN:
        raise HTTPException(
            status_code = 401,
            detail = constants.INVALID_EXPIRED_TOKEN
        )
    return token

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if not expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(hours=2)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    expire = datetime.now() + timedelta(days=7)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)