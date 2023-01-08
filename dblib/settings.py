from pydantic import BaseSettings, Field, PositiveInt


class Settings(BaseSettings):
    database_protocol: str = Field(env="DBLIB_PROTOCOL", default="sqlite")
    database_name: str = Field(env="DBLIB_NAME", default="/data.sqlite")
    database_username: str | None = Field(env="DBLIB_USERNAME", default=None)
    database_password: str | None = Field(env="DBLIB_PASSWORD", default=None)
    database_hostname: str | None = Field(env="DBLIB_HOSTNAME", default=None)
    database_port: PositiveInt | None = Field(env="DBLIB_PORT", default=None)
