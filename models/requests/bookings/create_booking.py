from pydantic import BaseModel, UUID4
from datetime import time


class CreateBookingRequest(BaseModel):

    user_id: UUID4
    show_id:UUID4
    payment_id:UUID4
    seat_nums: list[int]

    