from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config.settings import setting
db_url = f'postgresql://{setting.DB_USER}:{setting.POSTGRES_PASSWORD}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.POSTGRES_DB}'
engine = create_engine(db_url, echo=True)

declarative_base()
class Base:
    __name__: str

    @declared_attr
    def __table__(cls) -> str:
        return cls.__name__.lower()