from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.auth import get_current_user

router = APIRouter(prefix="/attendance", tags=["attendance"])


@router.get("")
async def list_attendance(current_user=Depends(get_current_user)) -> list[dict[str, str | None]]:
    if "attendance.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return [
        {
            "id": "att-001",
            "employee_name": "Muhammad Abubakar",
            "date": "2026-10-06",
            "check_in": "08:12",
            "check_out": "17:14",
            "status": "On time",
            "location": "YandyTech HQ",
        },
        {
            "id": "att-002",
            "employee_name": "Fatima Alhassan",
            "date": "2026-10-06",
            "check_in": "08:40",
            "check_out": "17:20",
            "status": "Late",
            "location": "YandyTech HQ",
        },
        {
            "id": "att-003",
            "employee_name": "Muktar Salis",
            "date": "2026-10-06",
            "check_in": "08:05",
            "check_out": "17:00",
            "status": "On time",
            "location": "YandyTech HQ",
        },
    ]


@router.post("/check-in")
async def check_in(current_user=Depends(get_current_user)) -> dict[str, str]:
    if "attendance.write" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return {
        "status": "checked_in",
        "employee": current_user.email or current_user.sub,
        "message": "Check-in recorded successfully.",
    }


@router.post("/check-out")
async def check_out(current_user=Depends(get_current_user)) -> dict[str, str]:
    if "attendance.write" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return {
        "status": "checked_out",
        "employee": current_user.email or current_user.sub,
        "message": "Check-out recorded successfully.",
    }
