from pydantic import BaseModel, ConfigDict, UUID4
from models.database.bookings.booking_status import BookingStatus

class CancelBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    status:BookingStatus