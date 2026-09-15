from pydantic import BaseModel, ConfigDict
from datetime  import datetime

class GetPaymentResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    amount:float
    status:int
    mode:int
    updated_at:datetime