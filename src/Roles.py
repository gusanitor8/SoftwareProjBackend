from enum import Enum


class Roles(Enum):
    # TODO roles preeliminares, se deben definir los roles de la aplicación
    # NOTA: Los nombres de las variables deben estar escritos exactamente iguak que en la base de datos
    # y exactamente igual que el valor de las variables (e.g. ADMIN = "admin")
    ADMIN = "admin"
    EDITOR = "editor"
    USER = "viewer"
