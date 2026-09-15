from pydantic import BaseModel, Field
from datetime import time
from domain.seats.seat import Seat


class GetBookingRequest(BaseModel):

    id:str = Field(
        min_length= 36,
        max_length= 36
    )

    user_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    