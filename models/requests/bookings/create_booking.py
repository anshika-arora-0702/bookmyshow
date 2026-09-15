from pydantic import BaseModel, Field
from datetime import time
from domain.seats.seat import Seat


class BookingCreateRequest(BaseModel):

    user_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    show_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    payment_mode:int

    seats: list[Seat]

    