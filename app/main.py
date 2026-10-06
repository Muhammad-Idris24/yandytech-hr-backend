from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logging import logger
from app.modules.attendance.router import router as attendance_router
from app.modules.employees.router import router as employees_router
from app.modules.leave.router import router as leave_router
from app.modules.organization.router import router as organization_router
from app.modules.payroll.router import router as payroll_router

app = FastAPI(
    title="YandyTech HR SaaS API",
    version="0.1.0",
    description="Secure multi-tenant HR SaaS backend.",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(organization_router, prefix="/api/v1")
app.include_router(employees_router, prefix="/api/v1")
app.include_router(attendance_router, prefix="/api/v1")
app.include_router(leave_router, prefix="/api/v1")
app.include_router(payroll_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    logger.info("healthcheck_requested")
    return {"status": "ok", "service": "yandytech-hr-backend"}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "YandyTech HR SaaS API is running"}
