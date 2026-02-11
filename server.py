from fastapi import FastAPI
from routes import (
    auth_routes, base_routes, user_routes
)
from middleware.logging_middleware import log_requests
from middleware.logging_middleware1 import LoggingMiddleware as LoggingMiddleware1

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

app.middleware("http")(log_requests)
app.add_middleware(LoggingMiddleware1)