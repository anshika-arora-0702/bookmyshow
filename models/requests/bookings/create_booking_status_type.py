from pydantic import BaseModel, UUID4, Field

class BookingStatusCreateRequest(BaseModel):

    id:int = Field(
        ge=1,
        le=99
    )

    user_id: UUID4

    name:str = Field(
        max_length = 100
    )
