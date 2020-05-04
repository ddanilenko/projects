from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import app

user = app.config.get("DB_USER")
password = app.config.get("DB_PASSWORD")
host = app.config.get("DB_HOST")

engine = create_engine(f'postgresql://{user}:{password}@{host}/tideas', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
