from faker_ka.core.db import Base
from sqlalchemy import Column, Integer, String


class FirstName(Base):
    """ORM model for user data."""
    __tablename__ = 'last_names'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
