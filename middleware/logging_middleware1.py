from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        print("\n*******************LoggingMiddleware1*****************************")
        print(f"{request.method} {request.url.path} completed in {duration:.4f}s")
        print("*******************LoggingMiddleware1*****************************\n")
        
        return response
