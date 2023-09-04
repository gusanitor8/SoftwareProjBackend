from config.database import Session
from models.Users import Users
from middlewares.hashing import hash_password

def get_pw_and_salt(email):
    session = Session()
    creds = session.query(Users.password, Users.salt).filter(Users.email == email).first()
    return creds


def verify_password(input_pw:str, db_pw:str, salt:str):
    verified_pw = False
    hashed_input = hash_password(input_pw, salt)

    if hashed_input == db_pw:
        verified_pw = True
    
    return verified_pw



    