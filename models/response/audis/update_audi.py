from pydantic import BaseModel, ConfigDict, UUID4

class UpdateAudiResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    cinema_id:UUID4
    type:int
    row_count:int
    column_count:int
    screen_num:int
    added_by:UUID4