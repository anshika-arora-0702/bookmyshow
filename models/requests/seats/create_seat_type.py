from pydantic import BaseModel, UUID4, Field

class SeatTypeCreateRequest(BaseModel):

    name:str = Field(
        max_length=50
    )

    user_id:UUID4