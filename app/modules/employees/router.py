from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.auth import get_current_user

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("")
async def list_employees(current_user=Depends(get_current_user)) -> list[dict[str, str | None]]:
    if "employee.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return [
        {
            "id": "emp-001",
            "full_name": "Muhammad Abubakar",
            "email": "muhammad.abubakar@yandytech.org",
            "department": "Technology & Research",
            "role": "Manager",
        },
        {
            "id": "emp-002",
            "full_name": "Fatima Alhassan",
            "email": "fatima.alhassan@yandytech.org",
            "department": "Youth, Workforce & Livelihood Development",
            "role": "Director",
        },
    ]


@router.get("/{employee_id}")
async def get_employee(employee_id: str, current_user=Depends(get_current_user)) -> dict[str, str | None]:
    if "employee.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    if employee_id == "emp-001":
        return {
            "id": employee_id,
            "full_name": "Muhammad Abubakar",
            "email": "muhammad.abubakar@yandytech.org",
            "department": "Technology & Research",
            "role": "Manager",
        }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
