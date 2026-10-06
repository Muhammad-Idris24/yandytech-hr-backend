from __future__ import annotations

from app.main import app
from app.modules.attendance.router import router as attendance_router

app.include_router(attendance_router, prefix="/api/v1")
