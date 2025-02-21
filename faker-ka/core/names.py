"""Module for faker names."""
from .base import FakerBase


class GeorgianNames(FakerBase):
    """Generates random georgian names."""

    def first_name(self, gender=None):
        """Return first name."""

        # if gender is None:


        return "saba"

    def last_name(self):
        """Return last name."""

        return "abzhandadze"

    def generate(self):
        """Return random full name."""

        return f"{self.first_name()} {self.last_name()}"


