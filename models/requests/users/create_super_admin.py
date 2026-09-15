from pydantic import BaseModel, Field
from datetime import date

class CreateSuperAdminRequest(BaseModel):

    first_name:str = Field(
        min_length = 3, 
        max_length = 20
    )

    last_name:str | None = Field(
        min_length = 3, 
        max_length = 20
    )

    role:str

    phone: str = Field(
        pattern=r"^(?:\+91[- ]?)?[6-9]\d{9}$"
    )

    email:str | None = Field(
        pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"
    )

    dob:date