from pydantic import BaseModel, UUID4
from models.database.seats.seat_type import SeatType

class CreateSeatRequest(BaseModel):

    audi_id: UUID4
    column_num:int
    row_char:str
    type:SeatType
    user_id:UUID4
    