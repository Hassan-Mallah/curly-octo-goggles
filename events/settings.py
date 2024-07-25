from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EVENTS_PORT: int = 5000
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@postgres/postgres"

    class Config:
        env_file = ".env"


settings = Settings()
