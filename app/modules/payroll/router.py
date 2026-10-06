from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.auth import get_current_user

router = APIRouter(prefix="/payroll", tags=["payroll"])


@router.get("")
async def list_payroll(current_user=Depends(get_current_user)) -> list[dict[str, str | float]]:
    if "payroll.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return [
        {
            "id": "pay-001",
            "employee_name": "Muhammad Abubakar",
            "period": "2026-10",
            "gross_salary": 4200000.0,
            "net_salary": 3695000.0,
            "status": "Approved",
            "currency": "NGN",
        },
        {
            "id": "pay-002",
            "employee_name": "Fatima Alhassan",
            "period": "2026-10",
            "gross_salary": 5100000.0,
            "net_salary": 4546000.0,
            "status": "Pending",
            "currency": "NGN",
        },
        {
            "id": "pay-003",
            "employee_name": "Muktar Salis",
            "period": "2026-10",
            "gross_salary": 2850000.0,
            "net_salary": 2556000.0,
            "status": "Approved",
            "currency": "NGN",
        },
    ]


@router.get("/summary")
async def payroll_summary(current_user=Depends(get_current_user)) -> dict[str, float | int | str]:
    if "payroll.read" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return {
        "total_monthly_run": 12150000.0,
        "approved": 2,
        "pending": 1,
        "currency": "NGN",
    }


@router.post("/{payroll_id}/approve")
async def approve_payroll(payroll_id: str, current_user=Depends(get_current_user)) -> dict[str, str]:
    if "payroll.write" not in current_user.permissions:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    return {
        "status": "approved",
        "payroll_id": payroll_id,
        "message": "Payroll approved successfully.",
    }
