from pydantic import BaseModel, Field

class GetShowSeatAvailabilityRequest(BaseModel):

    show_id:str = Field(
        min_length= 36,
        max_length= 36        
    )
    