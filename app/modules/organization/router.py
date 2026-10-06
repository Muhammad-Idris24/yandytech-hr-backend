from fastapi import APIRouter, Depends, HTTPException, status

from app.core.auth import get_current_user

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("")
async def list_organizations(current_user=Depends(get_current_user)) -> list[dict[str, str]]:
    if "organization.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return [
        {
            "id": "tenant_yandytech",
            "name": "YandyTech Community",
            "slug": "yandytech-community",
            "description": "First tenant and reference implementation.",
        },
        {
            "id": "tenant_organization_b",
            "name": "Organization B",
            "slug": "organization-b",
            "description": "Future tenant example.",
        },
    ]


@router.get("/{organization_id}")
async def get_organization(organization_id: str, current_user=Depends(get_current_user)) -> dict[str, str]:
    if "organization.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    if organization_id not in {"tenant_yandytech", "tenant_organization_b", "tenant_organization_c"}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")

    return {
        "id": organization_id,
        "name": "YandyTech Community" if organization_id == "tenant_yandytech" else "Other Organization",
        "slug": "yandytech-community" if organization_id == "tenant_yandytech" else "other-organization",
        "description": "Tenant configured for the YandyTech HR product.",
    }
