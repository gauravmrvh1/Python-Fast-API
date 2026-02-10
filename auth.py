from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import constants

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_token(token: str = Depends(oauth2_scheme)) -> str:
    if token != constants.FAKE_VALID_TOKEN:
        raise HTTPException(
            status_code = 401,
            detail = constants.INVALID_EXPIRED_TOKEN
        )
    return token


def verify_token(token: str):
    if token != constants.FAKE_VALID_TOKEN:
        raise HTTPException(
            status_code = 401,
            detail = constants.INVALID_EXPIRED_TOKEN
        )
    return token