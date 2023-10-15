from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class UsuarioRol(Base):
    __tablename__ = "usuario_rol"

    rol_usuarioID = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('usuarios.userID'))
    role_id = Column(Integer, ForeignKey('roles.roleID'))

    usuario = relationship("Usuarios")
    rol = relationship("Roles")