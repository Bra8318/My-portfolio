from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url : str
    cloud_name : str
    api_key:int
    api_secret:str

    class Config:
        env_file = "db.env"

setting = Settings()
