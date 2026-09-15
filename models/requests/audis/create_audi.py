from pydantic import BaseModel, UUID4, Field
from models.database.audis.audi_type import AudiType

class CreateAudiRequest(BaseModel):

    cinema_id:UUID4
    user_id:UUID4
    
#how to automate this int???
    screen_num:int = Field(
        ge=1,
        le=99 
    )

    row_count:int = Field(
        ge=1,
        le=99          
    )

    column_count:int = Field(
        ge=1,
        le=99
    )

    type:AudiType
    