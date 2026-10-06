from __future__ import annotations

from pydantic import BaseModel, Field


class AttendanceRecord(BaseModel):
    employee_name: str = Field(..., min_length=2, max_length=255)
    date: str = Field(..., min_length=8, max_length=10)
    check_in: str | None = None
    check_out: str | None = None
    status: str = Field(..., min_length=2, max_length=50)
    location: str | None = None


class AttendanceCheckInResponse(BaseModel):
    status: str
    employee: str
    message: str
