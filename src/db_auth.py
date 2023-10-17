from config.database import Session
from models.usuario_table import Usuario
from middlewares.hashing import hash_password
from datetime import datetime

def get_pw_and_salt(email) -> dict:
    try:
        session = Session()
        creds = session.query(Usuario.password, Usuario.salt).filter(Usuario.email == email).first()
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

def new_user(email, password, rol):
    try:
        session = Session()
        hashed_password, salt = hash_password(password)
        new_user = Usuario(email=email, password=hashed_password, salt=salt, rol=rol)
        session.add(new_user)
        session.commit()
    finally:
        session.close()

def get_jwt_credentials(email):
    try:
        session = Session()
        creds = session.query(Usuario.id_usuario, Usuario.rol).filter(Usuario.email == email).first()
        creds = creds._asdict()
        creds["iat"] = datetime.utcnow()

        return creds
    finally:
        session.close()


    