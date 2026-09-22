from pydantic import BaseModel, ConfigDict, UUID4

class FetchBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    payment_id:str
    status:int
    seats: list[UUID4]

    