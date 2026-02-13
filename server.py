from fastapi import FastAPI, Depends
from routes import (
    auth_routes, base_routes, user_routes
)
from middleware.logging_middleware import log_requests
from middleware.logging_middleware1 import LoggingMiddleware as LoggingMiddleware1

import services.auth as authService
import pika
import json


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



@app.post("/rabinMQ")
def register_user(
    email: str,
    _ = Depends(authService.get_current_user),
):
    publish_message({
        "name": "Gaurav Marvaha",
        "email": email
    })
    return {"message": "User registered. Email will be sent asynchronously."}


def publish_message(message: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="email_queue", durable=True)

    channel.basic_publish(
        exchange="",
        routing_key="email_queue",
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2  # persistent
        ),
    )

    connection.close()