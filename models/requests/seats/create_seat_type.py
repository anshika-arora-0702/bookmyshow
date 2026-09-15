from pydantic import BaseModel, Field

class SeatTypeCreateRequest(BaseModel):

    name:str = Field(
        max_length=50
    )

    user_id:str = Field(
        min_length=36,
        max_length=36
    )