from __future__ import annotations

from app.core.config import settings


def resolve_tenant_from_claims(claims: dict[str, object]) -> str:
    tenant_id = str(claims.get("tenant_id") or claims.get("organization_id") or "tenant_yandytech")
    if tenant_id not in settings.tenant_allowlist:
        raise ValueError(f"Unsupported tenant schema: {tenant_id}")
    return tenant_id


def current_tenant_schema(claims: dict[str, object]) -> str:
    return resolve_tenant_from_claims(claims)
