from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EVENTS_PORT: int = 5000

    class Config:
        env_file = ".env"


settings = Settings()
