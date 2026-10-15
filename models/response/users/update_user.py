from pydantic import BaseModel, ConfigDict, UUID4
from models.database.users.user_role import UserRole
from datetime import date

class UpdateUserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    id:UUID4
    first_name : str
    last_name : str | None = None
    role : UserRole
    phone : str
    email: str | None = None
    dob : date | None = None