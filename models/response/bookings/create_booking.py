from pydantic import BaseModel, ConfigDict

class CreateBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:str
    status:int
    