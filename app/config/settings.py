from pydantic import BaseSettings
from typing import Union
import os

class Settings(BaseSettings):

    SMARTSHEET_TOKEN: Union[str, None]
    DATABASE_URL: str
    DB_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    POSTGRES_DB: str

    class Config:

        env_file = ".env"
        env_file_encoding = "utf-8"

os.chdir("../..")
setting = Settings()