from pydantic import BaseModel, Field

class UpdateCityRequest(BaseModel):

    id: int = Field(
        gt=0
    )
    
    name:str = Field(
        max_length=50
    )
    