from fastapi import FastAPI, Depends
import auth
from routes import auth_routes, base_routes, user_routes

app = FastAPI(
    title="My API",
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(base_routes.router)
app.include_router(user_routes.router, prefix="/user", tags=["Users"])


@app.get("/search")
async def search(q: str, page: int = 1):
    return {"query": q, "page": page}

@app.get("/dashboard")
async def dashboard(token: str = Depends(auth.get_current_token)):
    auth.verify_token(token)
    return {
        "success": "true"
    }