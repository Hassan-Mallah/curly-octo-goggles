from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EVENTS_URL: str = "http://events:5000"
    ODDS_PORT: int = 5000

    class Config:
        env_file = ".env"


settings = Settings()
