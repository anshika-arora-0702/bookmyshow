from pydantic import BaseModel, UUID4

class FetchUserRequest(BaseModel):

    id : UUID4
    fetched_by : UUID4