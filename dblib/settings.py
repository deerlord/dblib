from typing import Optional

from pydantic import BaseSettings, Field, PositiveInt


class Settings(BaseSettings):
    database_protocol: str = Field(env="DBLIB_PROTOCOL", default="sqlite")
    database_name: str = Field(env="DBLIB_NAME", default="/data.sqlite")
    database_username: Optional[str] = Field(env="DBLIB_USERNAME", default=None)
    database_password: Optional[str] = Field(env="DBLIB_PASSWORD", default=None)
    database_hostname: Optional[str] = Field(env="DBLIB_HOSTNAME", default=None)
    database_port: Optional[PositiveInt] = Field(env="DBLIB_PORT", default=None)

    class Config:
        env_file = "/secrets/.dblib"
