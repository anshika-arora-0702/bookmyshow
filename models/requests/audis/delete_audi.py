from pydantic import BaseModel,  UUID4 , Field

class DeleteAudiRequest(BaseModel):

    id:UUID4
    user_id:UUID4
    