from pydantic import BaseModel, Field


class EmployeeBase(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=200)
    email: str = Field(..., min_length=3, max_length=255)
    department: str | None = None
    role: str | None = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeRead(EmployeeBase):
    id: str

    class Config:
        from_attributes = True
