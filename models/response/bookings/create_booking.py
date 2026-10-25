from pydantic import BaseModel, UUID4, ConfigDict
from models.database.bookings.booking_status import BookingStatus

class CreateBookingResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    status: BookingStatus
    payment_id: UUID4
    seat_ids: list[UUID4]