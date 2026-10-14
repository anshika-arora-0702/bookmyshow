from pydantic import BaseModel, ConfigDict, UUID4

class CreateUserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    first_name:str
    last_name:str | None = None