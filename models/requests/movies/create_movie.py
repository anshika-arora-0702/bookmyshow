from pydantic import BaseModel,UUID4, Field
from datetime import date

class CreateMovieRequest(BaseModel):

    name:str = Field(
        len = 100
    )

    user_id:UUID4

    poster:str | None = None

    runtime_in_sec:int = Field(
        ge = 1,
        le = 14400       
    )

    release_date:date 

    details:str | None = None
    