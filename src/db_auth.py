from config.database import Session
from models.Users import Users

def get_pw_and_salt(email):
    session = Session()
    creds = session.query(Users.password, Users.salt).filter(Users.email == email).first()
    return creds





    