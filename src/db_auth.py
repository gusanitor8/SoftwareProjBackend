from config.database import Session
from models.Users import Users
from middlewares.hashing import hash_password
from datetime import datetime

def get_pw_and_salt(email) -> dict:
    try:
        session = Session()
        creds = session.query(Users.password, Users.salt).filter(Users.email == email).first()
        creds = creds._asdict()
        return creds
    finally:
        session.close()

def verify_password(input_pw:str, db_pw:str, salt:str):
    verified_pw = False
    hashed_input, _ = hash_password(input_pw, salt)

    if hashed_input == db_pw:
        verified_pw = True
    
    return verified_pw

def new_user(email, password, role):
    try:
        session = Session()
        hashed_password, salt = hash_password(password)
        new_user = Users(email=email, password=hashed_password, salt=salt, role=role)
        session.add(new_user)
        session.commit()
    finally:
        session.close()

def get_jwt_credentials(email):
    try:
        session = Session()
        creds = session.query(Users.user_id, Users.role).filter(Users.email == email).first()
        creds = creds._asdict()
        creds["iat"] = datetime.utcnow()

        return creds
    finally:
        session.close()


    