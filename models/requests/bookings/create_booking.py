from pydantic import BaseModel, UUID4, Field
from decimal import Decimal

from models.database.payments.payment_mode import PaymentMode

class PaymentDetails(BaseModel):
    amount: Decimal = Field(gt = 0, decimal_places = 2)
    mode: PaymentMode

class CreateBookingRequest(BaseModel):

    user_id: UUID4
    show_id:UUID4
    seat_ids: list[UUID4]
    payment_details : PaymentDetails
    


    