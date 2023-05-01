from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str = 'postgres'
    DB_PASSWORD: str = 'root'
    DB_HOST: str = 'localhost'
    DB_NAME: str = 'spotlar'


settings = Settings()
