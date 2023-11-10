from fastapi.security import HTTPBearer
from fastapi import HTTPException
from middlewares.jwt_manager import validate_token


class JWTBearer(HTTPBearer):

    async def __call__(self, request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        user_id = data["id_usuario"]

        if user_id is not None:
            return user_id

        raise HTTPException(status_code=401, detail="Unauthorized")


def jwt_bearer(token: str):
    data = validate_token(token)
    user_id = None

    if data is not None:
        user_id = data["id_usuario"]

    if user_id is not None:
        return user_id

    raise HTTPException(status_code=401, detail="Unauthorized")

