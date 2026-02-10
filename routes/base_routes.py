from fastapi import APIRouter, HTTPException, Depends
import logging, Services.auth as auth

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
    return {
        "success": "true"
    }