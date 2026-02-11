from fastapi import APIRouter, Form, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.exc import IntegrityError
import schema.schemas as schemas
import schema.response as responseSchema
from sqlalchemy.orm import Session
import services.auth as authService
from services.user_service import UserService as UserServiceFromImport
import services.user_service as UserService
import models.models as models
import config.database as database, logging
from enum import Enum
from fastapi.responses import JSONResponse
import utils.response as responseUtil
import core.redis as redisCore
from fastapi import Query
from tasks import send_email_task
import tasks

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

CACHE_KEY = "users:list"
@router.post(
    "/users_list",
    # response_model=list[responseschema.UserResponse],
    description="Returns list of users",
    response_description= "Successful Response",
    response_model_by_alias=True,
)
def get_users(
    page: int = Query(1, ge=1, description="Page-number"),
    size: int = Query(10, ge=1, le=100, description="Page-size"),
    db: Session = Depends(database.get_db),
    _: str = Depends(authService.get_current_token)
):
    # # when response model added in route
    # return db.query(models.User).limit(1000).all()

    # response=UserServiceFromImport.get_user_list(page=page, db=db, size=size)
    response=UserService.UserService.get_user_list(page=page, db=db, size=size)
    data = response['data']
    # build success response
    return responseUtil.success_response(data, cached=response['meta']['cached'])

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
        
def send_email(email: str):
    print(f"Sending email to {email}")
    
@router.post("/register")
def register(email: str):
    tasks.send_email_task.delay(email)
    return {"message": "Task added to queue"}
# async def register(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(send_email, email)
#     return {"message": "User registered. Email will be sent."}