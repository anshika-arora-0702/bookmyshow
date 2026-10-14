from pydantic import BaseModel, ConfigDict, UUID4
from models.database.bookings.booking_status import BookingStatus

class FetchBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    payment_id: UUID4
    status: BookingStatus
    seats: list[UUID4]

    