from pydantic import BaseModel, ConfigDict

class CreateSeatResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:int
    audi_id:str
    type:int
    column_num:int
    row_char:str