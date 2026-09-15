from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote_plus

import os

db_user = os.getenv("DB_USER", "postgres")
db_password = quote_plus(os.getenv("DB_PASSWORD", "anshi@0702"))
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "bookmyshow")


db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

Engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = Engine )