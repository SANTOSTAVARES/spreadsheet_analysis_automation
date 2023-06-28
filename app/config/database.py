from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from settings import setting
from sqlalchemy.orm import sessionmaker


database_url = setting.DATABASE_URL
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()