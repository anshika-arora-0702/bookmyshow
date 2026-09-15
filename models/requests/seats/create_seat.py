from pydantic import BaseModel, Field

class SeatCreateRequest(BaseModel):

    audi_id:str = Field(
        min_length= 36,
        max_length= 36
    )

    column_num:int = Field(
        ge = 1,
        le=99
    )

    row_char:str = Field(
        max_length=2
    )

    type:int = Field(
        ge = 1,
        le=99
    )

    user_id:str = Field(
        min_length=36,
        max_length=36
    )
    