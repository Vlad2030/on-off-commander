from sqlalchemy import Column, Integer, String, DateTime, Boolean
from core.database import Base
from datetime import datetime


class UsersDatabase(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    token = Column(String, nullable=False, unique=True)
    token_expires_at = Column(DateTime)
    token_expired = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)
