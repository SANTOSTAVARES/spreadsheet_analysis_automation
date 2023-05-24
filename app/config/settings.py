from pydantic import BaseSettings
from typing import Union
import os

class Settings(BaseSettings):

    SMARTSHEET_TOKEN: Union[str, None]

    class Config:

        env_file = ".env"
        env_file_encoding = "utf-8"

os.chdir("../..")
setting = Settings()