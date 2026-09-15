from pydantic import BaseModel,  UUID4 , Field

class FetchAudiRequest(BaseModel):

    id:UUID4
    user_id:UUID4