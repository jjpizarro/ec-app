from pydantic import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    APP_ENV: str = 'dev'
    DATABASE_USERNAME: str = 'postgres'
    DATABASE_PASSWORD: str = '123123'
    DATABASE_HOST: str = 'localhost'
    DATABASE_NAME: str = 'myecapp'
    TEST_DATABASE_NAME: str = 'myecapp'
    SQLALCHEMY_DATABASE_URI: Optional[str] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

    class Config:
        case_sensitive: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
