from pydantic import BaseModel, constr


class UsuarioBase(BaseModel):
    """
    Esta clase indica los atributos que debe tener un usuario para ser creado.
    """
    password: constr(strip_whitespace=True, min_length=1)
    nombre: constr(strip_whitespace=True, min_length=1)
    email: constr(strip_whitespace=True, min_length=1)
    estado: bool
    rol: constr(strip_whitespace=True, pattern="^(viewer|editor|admin)$") = "viewer"

    class Config:
        from_attributes = True


class UsuarioLogIn(BaseModel):
    """
    Esta clase indica los atributos que debe tener un usuario para hacer el Log In
    """
    email: constr(strip_whitespace=True, min_length=1)
    password: constr(strip_whitespace=True, min_length=1)

    class Config:
        from_attributes = True


class UsuarioSelect(BaseModel):
    """
    Esta clase sirve solamente para indicar el input del correo del usuario
    """

    email: constr(strip_whitespace=True, min_length=1)

    class Config:
        from_attributes = True

