from pydantic import BaseModel, UUID4

class CancelBookingRequest(BaseModel):

    id:UUID4
    user_id:UUID4