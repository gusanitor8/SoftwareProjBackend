from ..middlewares.jwt_manager import create_token

def test_create_token():
    token = create_token({"username": "test", "password": "test"})
    pass