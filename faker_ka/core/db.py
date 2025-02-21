"""Database related functions."""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from .constants import Constants

Base = declarative_base()

from faker_ka.models.first_name import User
from faker_ka.models.address import Address


class Database:
    """Handles database connection using SQLAlchemy."""

    def __init__(self, db_url=None):
        self.config = Constants()
        self.engine = create_engine(db_url or self.config.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

