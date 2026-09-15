from pydantic import BaseModel, Field
from datetime import date

class CreateMovieRequest(BaseModel):

    name:str = Field(
        len = 100
    )

    user_id:str = Field(
        min_length=36,
        max_length=36
    )

    poster:str | None = None

    runtime_in_sec:int | None = Field(
        ge = 1,
        le = 28800         
    )

    release_date:date | None = None

    details:str | None = None
    