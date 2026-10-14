from pydantic import BaseModel, UUID4
from datetime import date

class GetShowRequest(BaseModel):

    id: UUID4
    