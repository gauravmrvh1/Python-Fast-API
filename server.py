from fastapi import FastAPI
from routes import (
    auth_routes, base_routes, user_routes
)

app = FastAPI(
    debug=True,
    title="Gaurav Marvaha",
    docs_url="/swagger",
    redoc_url="/redoc-swagger",
    openapi_url="/swagger.json",
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth Module"])
app.include_router(base_routes.router, tags=["Home Module"])

app.include_router(
    user_routes.router,
    # prefix="/user",
    # tags=["Users"]
)