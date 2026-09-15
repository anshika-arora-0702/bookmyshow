from pydantic import BaseModel, ConfigDict
from domain.seats.seat import Seat

class GetBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    payment_id:str
    status:int
    seats: list[Seat]

    