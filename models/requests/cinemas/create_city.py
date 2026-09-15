from pydantic import BaseModel, Field

class CreateCityRequest(BaseModel):

    name:str = Field(
        max_length=50
    )

    user_id: str = Field(
        max_length=36,
        min_length=36
    )
    