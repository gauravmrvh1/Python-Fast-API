from fastapi import APIRouter, Form, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
import Schema.schemas as schemas
import Schema.response as responseSchema
from sqlalchemy.orm import Session
import Services.auth as authService
from Services.user_service import UserService
import Models.models as models
import Config.database as database, logging
from enum import Enum
from fastapi.responses import JSONResponse
import utils.response as responseUtil

class Tags(Enum):
    USERS = "Users Module"
    ADMIN = "Admin"
    
router = APIRouter(
    # prefix="/users-routes", # URL prefix
    tags=[Tags.USERS], # Swagger grouping
    dependencies=[Depends(authService.get_current_token)], # Router-level auth
    default_response_class=JSONResponse,  # Default response type
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
    },
    redirect_slashes=True, # /users → /users/
    deprecated=False, # Mark whole router deprecated
    include_in_schema=True, # Show in Swagger
)

logger = logging.getLogger(__name__)

@router.post(
    "/users_list",
    # response_model=list[responseSchema.UserResponse],
    description="Returns list of users",
    response_description= "Successful Response",
    response_model_by_alias=True,
)
def get_users(
    page: int = 1,
    size: int = 2,
    db: Session = Depends(database.get_db),
    _: str = Depends(authService.get_current_token)
):
    # return UserService.get_user_list(db)
    users = UserService.get_user_list(db, page, size)
    return responseUtil.success_response(users)
    return db.query(models.User).limit(1000).all()

@router.get("/{user_id}")
async def get_user(
    user_id: int
):
    return {"user_id": user_id}

@router.post("/")
async def create_user_form(
    name: str = Form(...),
    email: str = Form(...),
    mobile_number: int = Form(...),
    db: Session = Depends(database.get_db),
    _: str = Depends(authService.get_current_user)
):
    try:
        user = models.User(name=name, email=email, mobile_number=mobile_number)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except Exception as e:
        logger.exception(str(e))
        raise HTTPException(
            status_code = 500,
            detail=str(e)
        )

@router.post(
    "/create-user",
    response_model=schemas.User,
    status_code=status.HTTP_201_CREATED
)
async def create_users(
    user: schemas.User,
    db: Session = Depends(database.get_db),
    _: str = Depends(authService.get_current_token)
):
    try:
        db_user = models.User(
            name = user.name,
            email = user.email,
            mobile_number = user.mobile_number,
            aadhar_number = user.aadhar_number,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except IntegrityError as e:
        logger.exception(str(e))
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            # detail="User with same email or aadhar already exists",
            detail=str(e)
        )

    except Exception as e:
        logger.exception(str(e))
        db.rollback()
        raise HTTPException(
            status_code = 500,
            detail=str(e)
        )
        
@router.post(
    "/create-admin",
    response_model=schemas.Admin,
    status_code=status.HTTP_201_CREATED
)
async def create_admin_user(
    user: schemas.Admin,
    db: Session = Depends(database.get_db),
    _: str = Depends(authService.get_current_token)
):
    try:
        db_user = models.Admin(
            first_name = user.f_name,
            last_name = user.l_name,
            username = user.username,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except IntegrityError as e:
        logger.exception(str(e))
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

    except Exception as e:
        logger.exception(str(e))
        db.rollback()
        raise HTTPException(
            status_code = 500,
            detail=str(e)
        )