import os
from dotenv import load_dotenv
from dataclasses import dataclass, field

load_dotenv()


@dataclass(frozen=True)
class Constants:
    """Constants used for application."""

    DATABASE_URL: str = field(default_factory=lambda: os.getenv("DATABASE_URL"))
    EXTERNAL_DB_URL: str = field(default_factory=lambda: os.getenv("EXTERNAL_DB_URL"))
    DEBUG: bool = field(default_factory=lambda: os.getenv("DEBUG"))

