from pydantic import BaseModel, ConfigDict, UUID4

class CancelBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    status:int
    payment_id:str
    seats: list[UUID4]