from pydantic import BaseModel, Field
from datetime import date

class GetShowRequest(BaseModel):

    movie_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    date:date
    