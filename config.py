import os
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    mysql_user:str
    mysql_password:int
    mysql_database:str
    mysql_host:str
    mysql_port:int

    def database_url(self) -> str:
        return (
            f"mysql+pymysql://{self.mysql_user}:{quote_plus(str(self.mysql_password))}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}?charset=utf8mb4"
        )
settings=Settings()


