from pydantic import BaseModel, UUID4, Field, EmailStr
from datetime import date

class UpdateUserRequest(BaseModel):

    updated_by : UUID4
    first_name : str | None = Field(default=None, min_length=3, max_length=20)
    last_name : str | None = Field(default=None, min_length=3, max_length=20)
    phone: str | None = Field( default = None, pattern=r"^[6-9]\d{9}$")
    email: EmailStr | None = None
    dob : date | None = None
