from pydantic import BaseModel, ConfigDict

class AudiTypeCreateResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    name:str
    