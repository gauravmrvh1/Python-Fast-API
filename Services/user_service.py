from sqlalchemy.orm import Session
import Models.models as models

class UserService:

    @staticmethod
    def get_user_list(db: Session):
        return db.query(models.User).limit(1000).all()
