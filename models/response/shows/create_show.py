from pydantic import BaseModel, ConfigDict

class CreateShowResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    audi_id:str
    movie_id:str