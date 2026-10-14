from pydantic import BaseModel, ConfigDict, UUID4
from models.database.audis.audi_type import AudiType

class CreateAudiResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    cinema_id:UUID4
    type: AudiType
    
    