from pydantic import BaseModel, UUID4,  PositiveFloat

from datetime import datetime
from models.database.seats.seat_type import SeatType

class CreateShowRequest(BaseModel):

    audi_id:UUID4
    movie_id: UUID4
    user_id:UUID4
    start_time: datetime
    price: dict[SeatType, PositiveFloat]

    