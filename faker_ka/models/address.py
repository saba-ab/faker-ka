from faker_ka.core.db import Base
from sqlalchemy import Column, String, Integer


class Address(Base):
    """ORM model for address data."""
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(50),  nullable=False)
    city = Column(String(50), nullable=False)
