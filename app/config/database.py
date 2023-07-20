from sqlalchemy import create_engine
from app.config.settings import setting
from sqlalchemy.orm import sessionmaker, declarative_base


database_url = setting.DATABASE_URL
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
