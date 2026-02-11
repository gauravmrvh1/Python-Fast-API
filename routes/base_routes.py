from fastapi import APIRouter, HTTPException, Depends
import logging, Services.auth as auth
import redis
from utils import response
import utils.response as utilResponse
import Config.redis as redisSettings
from core.redis import redis_client
import core.redis as redisCore

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
async def root():
    try:
        # force exception for testing
        raise ValueError("Custom error message..")

        return {
            "success": True,
            "data": {
                "message": "Hello FastAPI"
            }
        }

    except ValueError as e:
        logger.info("Value error in root route")

        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "error": {
                    "code": "BAD_REQUEST",
                    "message": str(e)
                }
            }
        )

    except Exception as e:
        logger.exception("Unhandled error")

        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "Something went wrong. Please try again later."
                }
            }
        )

@router.get("/search")
async def search(q: str, page: int = 1):
    return {"query": q, "page": page}


@router.get("/dashboard")
async def dashboard(_: str = Depends(auth.get_current_user)):
    # ####################################################################
    # r = redis.Redis(
    #     host=redisSettings.REDIS_HOST,
    #     port=redisSettings.REDIS_PORT,
    #     decode_responses=True
    # )
    # r.set("name", "Gaurav Marvaha")
    # ####################################################################

    # #####################################################################
    # redis_client.set(key="name", value="Gaurav Marvaha", ttl=60)
    # redis_client.set(key="mobile", value=8881438096, ttl=60)
    # redis_client.set(key="address", value="Hapur", ttl=60)
    # #####################################################################
    
    # ####################################################################
    # for k, v in {"name": "Ankit", "mobile": 895019178787, "address": "Hapur"}.items():
    #     redis_client.set(k, v, ttl=120)
    # ####################################################################


    # redis_client.client.hset("user:1", mapping={"name": "Gaurav Marvaha", "mobile": 8881438096, "address": "Hapur"})

    data = {
        "name" : redisCore.redis_client.get(key="name"),
        "mobile" : redis_client.get(key="mobile"),
        "address" : redis_client.get(key="address"),
    }
    return utilResponse.success_response(data)
    return response.success_response(r.get("name"))