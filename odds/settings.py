from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EVENTS_URL: str = "http://events:5000"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@postgres/postgres"
    ODDS_PORT: int = 5000

    class Config:
        env_file = ".env"


settings = Settings()
