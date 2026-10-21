from pydantic import BaseModel, UUID4, Field

class CreateCinemaRequest(BaseModel):

    name:str
    address:str | None = None
    user_id:UUID4
    city:int = Field(
        ge = 1
    )

    