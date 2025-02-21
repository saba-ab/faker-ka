from faker_ka.core.faker import Faker
from faker_ka.core.constants import Constants
from faker_ka.core.db import Database


def main():
    db = Database()
    db.create_tables()  # Ensure tables are created
    print("✅ Database tables created successfully!")
    faker = Faker()


if __name__ == "__main__":
    main()
