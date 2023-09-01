from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from typing import Tuple

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) ->  Tuple[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse({"message": str(e)}, status_code=500)