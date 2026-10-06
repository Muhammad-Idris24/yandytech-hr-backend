from __future__ import annotations

from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from pydantic import BaseModel

from app.core.config import settings

security = HTTPBearer(auto_error=False)


class AuthenticatedUser(BaseModel):
    sub: str
    tenant_id: str | None = None
    roles: list[str] = []
    permissions: list[str] = []
    email: str | None = None


def _build_dev_user() -> AuthenticatedUser:
    return AuthenticatedUser(
        sub="dev-user",
        tenant_id="tenant_yandytech",
        roles=["hr_admin", "manager"],
        permissions=[
            "organization.read",
            "organization.write",
            "employee.read",
            "employee.write",
            "payroll.read",
            "payroll.write",
            "attendance.read",
            "attendance.write",
            "leave.read",
            "leave.write",
        ],
        email="dev@yandytech.org",
    )


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> AuthenticatedUser:
    if settings.auth0_disabled:
        return _build_dev_user()

    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            settings.auth0_audience,
            algorithms=[settings.auth0_algorithms],
            issuer=settings.auth0_issuer,
            options={"verify_aud": True, "verify_exp": True},
        )
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        ) from exc

    return AuthenticatedUser(
        sub=str(payload.get("sub", "unknown-user")),
        tenant_id=str(payload.get("tenant_id") or payload.get("organization_id") or "tenant_yandytech"),
        roles=list(payload.get("roles", [])),
        permissions=list(payload.get("permissions", [])),
        email=payload.get("email"),
    )
