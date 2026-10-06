from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    debug: bool = True
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/yandytech_hr"
    auth0_domain: str = "your-tenant.auth0.com"
    auth0_audience: str = "https://yandytech-hr-api"
    auth0_issuer: str = "https://your-tenant.auth0.com/"
    auth0_algorithms: str = "RS256"
    auth0_disabled: bool = True
    allowed_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://yandytech.org",
    ]
    tenant_allowlist: list[str] = ["tenant_yandytech", "tenant_organization_b", "tenant_organization_c"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def allowed_origins_list(self) -> list[str]:
        return self.allowed_origins


settings = Settings()
