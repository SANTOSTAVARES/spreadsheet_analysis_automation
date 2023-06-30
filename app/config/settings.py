from pydantic import BaseSettings
from typing import Union
import os

class Settings(BaseSettings):

    SMARTSHEET_TOKEN: Union[str, None]
    DATABASE_URL: Union[str, None]
    DB_USER: Union[str, None]
    POSTGRES_PASSWORD: Union[str, None]
    DB_HOST: Union[str, None]
    DB_PORT: Union[str, None]
    POSTGRES_DB: Union[str, None]

    class Config:

        env_file = ".env"
        env_file_encoding = "utf-8"

os.chdir("../..")
setting = Settings()