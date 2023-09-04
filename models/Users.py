from config.database import Base
from sqlalchemy import Column, BigInteger, String, Index

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)
    role = Column(String)

    # Create an index on the primary key (user_id)
    __table_args__ = (
        Index('idx_user_id', user_id),
    )

    # Create an index on the email column
    __table_args__ += (
        Index('idx_email', email),
    )