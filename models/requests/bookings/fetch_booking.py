from pydantic import BaseModel, UUID4

class FetchBookingRequest(BaseModel):

    id:UUID4
    user_id:UUID4

    