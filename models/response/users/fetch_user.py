from pydantic import BaseModel, ConfigDict, UUID4
from models.database.users.user_role import UserRole
from datetime import date

class FetchUserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    first_name : str
    last_name : str
    role : UserRole
    phone : str
    email: str
    dob : date