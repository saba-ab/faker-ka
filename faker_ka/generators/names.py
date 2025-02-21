"""Module for faker names."""
from .base import FakerBase
from faker_ka.core.db import Database
from faker_ka.models.first_name import User
import random


class GeorgianNames(FakerBase):
    """Generates random georgian names."""

    def __init__(self):
        super().__init__()
        self.db = Database().get_session()

    def first_name(self, gender=None):
        """Return first name."""

        query = self.db.query(User.first_name)

        if gender:
            query = query.filter(User.gender == gender)

        first_names = query.all()
        if not first_names:
            return "Unknown"

        return random.choice(first_names)[0]

    def last_name(self):
        """Return a random last name from the database."""

        last_names = self.db.query(User.last_name).all()

        if not last_names:
            return "Unknown"

        return random.choice(last_names)[0]

    def generate(self):
        """Return random full name."""

        return f"{self.first_name()} {self.last_name()}"


