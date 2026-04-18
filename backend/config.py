from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url : str

    class Config:
        env_file = "db.env"

setting = Settings()
