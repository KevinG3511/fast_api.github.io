from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuracion"""
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50

    class Config:
        env_file= ".env"

settings = Settings()
