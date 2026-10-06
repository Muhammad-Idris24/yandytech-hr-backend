from __future__ import annotations

from pydantic import BaseModel, Field


class PayrollRecord(BaseModel):
    employee_name: str = Field(..., min_length=2, max_length=255)
    period: str = Field(..., min_length=6, max_length=12)
    gross_salary: float
    net_salary: float
    status: str = Field(..., min_length=2, max_length=50)
    currency: str = Field(default="NGN", min_length=2, max_length=10)


class PayrollSummary(BaseModel):
    total_monthly_run: float
    approved: int
    pending: int
    currency: str
