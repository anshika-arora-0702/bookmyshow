from pydantic import BaseModel, ConfigDict

class GetSeatAvailabilityResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    seat_id:str
    availability:bool


class GetShowAllSeatsAvailabilityResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    seats: list[GetSeatAvailabilityResponse]

    