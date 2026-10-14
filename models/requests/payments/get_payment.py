from pydantic import BaseModel, UUID4

class GetPaymentRequest(BaseModel):

    id: UUID4
    user_id: UUID4