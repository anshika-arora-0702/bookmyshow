from pydantic import BaseModel, ConfigDict
from domain.seats.seat import Seat

class BookingCreateResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    status:int
    