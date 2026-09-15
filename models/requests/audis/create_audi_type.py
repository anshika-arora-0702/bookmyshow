from pydantic import BaseModel, UUID4, Field

class CreateAudiTypeRequest(BaseModel):

    name:str = Field(
        min_length = 1, 
        max_length = 30
    )

    user_id:UUID4

    