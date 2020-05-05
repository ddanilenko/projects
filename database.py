from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import app

user = app.config.get("DB_USER")
password = app.config.get("DB_PASSWORD")
host = app.config.get("DB_HOST")
db_url = f'postgresql://{user}:{password}@{host}/tideas'

engine = create_engine(db_url, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
