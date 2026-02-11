from fastapi import Request
import time

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    print("\n*******************LoggingMiddleware*****************************")
    print(f"{request.url.path} completed in {duration}")
    print("*******************LoggingMiddleware*****************************\n")

    return response
