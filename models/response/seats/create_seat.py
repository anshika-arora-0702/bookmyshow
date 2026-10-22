from pydantic import BaseModel,UUID4, ConfigDict
from models.database.seats.seat_type import SeatType

class CreateSeatResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    audi_id: UUID4
    type:SeatType
    column_num:int
    row_char:str