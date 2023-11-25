from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import setting

database_url = setting.DATABASE_URL
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
