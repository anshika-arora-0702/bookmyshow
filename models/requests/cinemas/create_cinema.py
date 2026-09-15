from pydantic import BaseModel, Field

class CreateCinemaRequest(BaseModel):

    name:str
    address:str | None = None
    user_id:str = Field(
        min_length=36,
        max_length=36
    )

    city:int = Field(
        ge = 1
    )

    