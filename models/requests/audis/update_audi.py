from pydantic import BaseModel,  UUID4 , Field

class UpdateAudiRequest(BaseModel):

    id:UUID4
    user_id:UUID4
    cinema_id:UUID4
    type:int
    row_count:int
    column_count:int
    screen_num:int