from pydantic import BaseModel, UUID4, Field

class GetShowSeatAvailabilityRequest(BaseModel):

    show_id:UUID4
    