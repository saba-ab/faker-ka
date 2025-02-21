from faker_ka.core.db import Database
from faker_ka.core.constants import Constants

config = Constants()


def fetch_external_data():
    external_db = Database(db_url=config.EXTERNAL_DB_URL)
    # query