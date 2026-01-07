from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações da aplicação."""

    DB_URL: str = Field(
        ...,
        description="URL de conexão com o banco de dados",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
