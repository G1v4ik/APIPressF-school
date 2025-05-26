from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = 'local'
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DATABASE: str = "postgresql+asyncpg://forge:HIITeig1or2$@77.223.101.104:5432/api_pressf_inc"
    RELOAD: bool = False

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    settings = Settings()
    return settings