from fastapi import FastAPI
from routes import auth_routes, base_routes, user_routes

app = FastAPI(
    title="My API",
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(base_routes.router, tags=["Home"])
app.include_router(user_routes.router, prefix="/user", tags=["Users"])