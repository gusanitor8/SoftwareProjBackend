from jwt import encode, decode, exceptions
import os

def create_token(data) -> str:
    key = os.getenv("SECRET_KEY")
    token : str = encode(payload=data, key=key, algorithm="HS256")
    return token

def validate_token(token) -> dict:
    key = os.getenv("SECRET_KEY")
    try:
        data: dict = decode(token, key=key, algorithms=["HS256"])
        return data
    except exceptions.DecodeError as e:
        # Handle the invalid token exception here
        print(f"Invalid token: {e}")
        return None
