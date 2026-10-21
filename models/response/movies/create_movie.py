from pydantic import BaseModel, UUID4, ConfigDict

class CreateMovieResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    name:str