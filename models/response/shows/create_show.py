from pydantic import BaseModel, UUID4, PositiveFloat, ConfigDict
from datetime import datetime
from models.database.seats.seat_type import SeatType

class CreateShowResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    audi_id: UUID4
    movie_id: UUID4
    start_time: datetime
    price: dict[SeatType, PositiveFloat]


