from pydantic import BaseModel, UUID4

from models.database.payments.payment_mode import PaymentMode

class CreateBookingRequest(BaseModel):

    user_id: UUID4
    show_id:UUID4
    seat_ids: list[UUID4]
    payment_mode : PaymentMode
    


    