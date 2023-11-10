from config.database import Session
from models.usuario_table import Usuario
from middlewares.hashing import hash_password
from datetime import datetime
from src.Roles import Roles
from middlewares.jwt_manager import validate_token

def get_pw_and_salt(email) -> dict:
    try:
        session = Session()
        creds = session.query(Usuario.password, Usuario.salt).filter(Usuario.email == email).first()

        if creds is None:
            return {}
        else:
            creds = creds._asdict()
            return creds

    finally:
        session.close()


def user_is_active(email) -> bool:
    try:
        session = Session()
        user = session.query(Usuario.estado).filter(Usuario.email == email).first()

        if user is None:
            # Se devuelve True porque si el usuario no existe entonces no levante el error
            # de usuario desactivado
            return True
        else:
            return user[0]

    finally:
        session.close()


def verify_password(input_pw: str, db_pw: str, salt: str):
    verified_pw = False
    hashed_input, _ = hash_password(input_pw, salt)

    if hashed_input == db_pw:
        verified_pw = True

    return verified_pw


def new_user(email, password, rol, name):
    try:
        session = Session()
        hashed_password, salt = hash_password(password)
        new_user = Usuario(
            nombre=name,
            estado=True,
            email=email,
            password=hashed_password,
            salt=salt,
            rol=rol)

        session.add(new_user)
        session.commit()
    finally:
        session.close()


def get_jwt_credentials(email):
    """
    Esta funcion devuelve el payload para el JWT
    """
    session = Session()

    try:
        creds = session.query(Usuario.id_usuario, Usuario.rol).filter(Usuario.email == email).first()
        creds = creds._asdict()
        creds["iat"] = datetime.utcnow()

        return creds
    finally:
        session.close()


def delete_user(email: str) -> bool:
    """
    Esta funcion borra un usuario de la base de datos, regresa verdadero si se borro correctamente o falso si
    el usuario no existe
    """
    try:
        session = Session()
        result = session.query(Usuario).filter(Usuario.email == email)

        if not result.first():
            return False

        result.delete()
        session.commit()

        return True
    finally:
        session.close()


def alter_user_state(email: str, state: bool) -> bool:
    try:
        session = Session()
        result = session.query(Usuario).filter(Usuario.email == email)

        if not result.first():
            return False

        result.update({"estado": state})
        session.commit()
        return True
    finally:
        session.close()

def update_user_permissions(email: str, role: str) -> bool:
    try:
        session = Session()
        result = session.query(Usuario).filter(Usuario.email == email)

        if not result.first():
            return False

        result.update({"rol": role})
        session.commit()
        return True
    finally:
        session.close()

def get_role(user_id: int):
    try:
        session = Session()
        result = session.query(Usuario.rol).filter(Usuario.id_usuario == user_id).first()

        if not result:
            return None

        return result[0]

    finally:
        session.close()

def roles_match(user_id: int, required_role: Roles) -> bool:
    """
    Esta funcion regresa verdadero si el rol del usuario es el mismo que el rol requerido
    """
    role = get_role(user_id)

    if role is not None:
        if role == required_role.value:
            return True

    return False