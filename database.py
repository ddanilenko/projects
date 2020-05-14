import json
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open(os.path.abspath(os.path.join('config/config.json', ))) as f:
    config = json.load(f)

user = config.get("DB_USER")
password = config.get("DB_PASSWORD")
host = config.get("DB_HOST")
db_name = config.get("DB_NAME")
db_url = f'postgresql://{user}:{password}@{host}/{db_name}'

engine = create_engine(db_url, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
