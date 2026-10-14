from pydantic import BaseModel, UUID4, Field
from models.database.seats.seat_type import SeatType

class SeatCreateRequest(BaseModel):

    audi_id: UUID4
    column_num:int
    row_char:str
    type:SeatType
    user_id:UUID4
    