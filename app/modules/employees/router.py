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
        {
            "id": "emp-003",
            "full_name": "Muktar Salis",
            "email": "muktar.salis@yandytech.org",
            "department": "HR",
            "role": "Admin and Operations Officer",
        },
    ]


@router.get("/{employee_id}")
async def get_employee(employee_id: str, current_user=Depends(get_current_user)) -> dict[str, str | None]:
    if "employee.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    employee_map = {
        "emp-001": {
            "id": "emp-001",
            "full_name": "Muhammad Abubakar",
            "email": "muhammad.abubakar@yandytech.org",
            "department": "Technology & Research",
            "role": "Manager",
        },
        "emp-002": {
            "id": "emp-002",
            "full_name": "Fatima Alhassan",
            "email": "fatima.alhassan@yandytech.org",
            "department": "Youth, Workforce & Livelihood Development",
            "role": "Director",
        },
        "emp-003": {
            "id": "emp-003",
            "full_name": "Muktar Salis",
            "email": "muktar.salis@yandytech.org",
            "department": "HR",
            "role": "Admin and Operations Officer",
        },
    }

    employee = employee_map.get(employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    return employee
