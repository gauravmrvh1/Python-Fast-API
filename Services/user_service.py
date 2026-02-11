from sqlalchemy.orm import Session
import Models.models as models

class UserService:

    @staticmethod
    def get_user_list(
        db: Session,
        page: int,
        size: int,
    ):
        offset = (page - 1) * size
        return db.query(models.User).offset(offset).limit(size).all()
