from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

from app import log


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False
    database_url: AnyUrl = None


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the enviroment...")
    return Settings()
