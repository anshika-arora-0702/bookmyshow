from pydantic import BaseModel, ConfigDict, PositiveFloat
from datetime import datetime

class GetShowResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    audi_id:str
    movie_id:int
    start_time:datetime
    price: dict[int, PositiveFloat]