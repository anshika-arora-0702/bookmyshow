from pydantic import BaseModel, ConfigDict

class CreateCityResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:int
    name:str