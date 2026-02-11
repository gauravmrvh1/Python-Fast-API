from sqlalchemy.orm import Session
import Models.models as models
from core.redis import redis_client

class UserService:

    @staticmethod
    def get_user_list(
        db: Session,
        page: int,
        size: int,
    ):
        offset = (page - 1) * size
        cache_key = f"users:list:page:{page}:size:{size}"
        
        cached = redis_client.get(cache_key)
        if cached: 
            return {
                "data" :cached,
                "meta": {
                    "cached": True
                }
            }
        
        users = db.query(models.User).offset(offset).limit(size).all()
        users_data = [
            {
                "id": u.id,
                "name": u.name,
                "email": u.email
            }
            for u in users
        ]
        redis_client.set(cache_key, users_data, ttl=60)
        return {
            "data" :users_data,
            "meta": {
                "cached": False
            }
        }
