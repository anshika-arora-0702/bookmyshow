from pydantic import BaseModel, Field
from datetime import date
from models.database.users.user_role import UserRole

class CreateUserRequest(BaseModel):

    first_name:str = Field(
        min_length = 3, 
        max_length = 20
    )

    last_name:str | None = Field(
        default = None,
        min_length = 3, 
        max_length = 20
    )

    phone: str = Field(
        pattern=r"^[6-9]\d{9}$"
    )

    email:str | None = Field(
        default = None,
        pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$",
        max_length= 100,
        examples = ["aarav@example.com"]
    )

    dob:date
    password: str
    