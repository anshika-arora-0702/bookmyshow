from pydantic import BaseModel, Field, PositiveFloat
from datetime import time

class ShowCreateRequest(BaseModel):

    audi_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    movie_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    user_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    start_time:time
    price: dict[int, PositiveFloat]

    