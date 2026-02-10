from fastapi import APIRouter, Form, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
import Schema.schemas as schemas
from sqlalchemy.orm import Session
import Services.auth as auth, Models.models as models, Config.database as database, logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/users_list")
def get_users(
    db: Session = Depends(database.get_db),
    _: str = Depends(auth.get_current_token)
):
    return db.query(models.User).limit(1000).all()

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.post("/")
async def create_user_form(
    name: str = Form(...),
    email: str = Form(...),
    mobile_number: int = Form(...),
    db: Session = Depends(database.get_db),
    _: str = Depends(auth.get_current_token)
):
    user = models.User(name=name, email=email, mobile_number=mobile_number)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post(
    "/create-user",
    response_model=schemas.User,
    status_code=status.HTTP_201_CREATED
)
async def create_users(
    user: schemas.User,
    db: Session = Depends(database.get_db),
    _: str = Depends(auth.get_current_token)
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
    _: str = Depends(auth.get_current_token)
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