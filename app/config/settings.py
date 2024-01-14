from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    SMARTSHEET_TOKEN: str
    DATABASE_URL: str
    REAL_EMAIL: str
    REAL_USER_NAME: str
    REAL_SHEET_NAME: str
    REAL_MAIN_COLUMN: str
    TASK_TYPE: str
    AUXILIARY_COLUMN: str | None
    REFERENCE_VALUES: str
    POSTGRES_PASSWORD: str | int

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")


setting = Settings()
