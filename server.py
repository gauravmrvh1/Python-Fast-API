from fastapi import FastAPI, Depends
from routes import (
    auth_routes, base_routes, user_routes
)
from middleware.logging_middleware import log_requests
from middleware.logging_middleware1 import LoggingMiddleware as LoggingMiddleware1

import services.auth as authService
import threading
from multiprocessing import Process
from producer.add_email_producer import publish_email_message
from producer.add_task_producer import start_publish_task

from consumer.email_consumer import start_email_consumer
from consumer.add_task_consumer import start_task_consumer


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

# app.middleware("http")(log_requests)
# app.add_middleware(LoggingMiddleware1)


WORKERS = [start_email_consumer,start_task_consumer,]

@app.on_event("startup")
def start_workers():
    print('********** Hello **************************')
    # ### Start Worker Individually #######################
    #     threading.Thread(target=start_email_consumer, daemon=True).start()
    #     threading.Thread(target=start_task_consumer, daemon=True).start()

    ############ Threads for I/O bound Single Thread #################
    # for worker in WORKERS:
    #     threading.Thread(target=worker, daemon=True).start()
    ##################################################################
    
    ######### For CPU heavy tasks Starting 4 Consumers Here ########## 
    # for _ in range(2):
    #     Process(target=start_email_consumer).start()
    #     Process(target=start_task_consumer).start()
    ##################################################################


@app.post("/rabinMQ")
def register_user(
    email: str,
    _ = Depends(authService.get_current_user),
):
    emailData = {"name": "Gaurav Marvaha","email": email}
    publish_email_message(emailData)
    
    start_publish_task()
    
    return {"message": "User registered. Email will be sent asynchronously."}


