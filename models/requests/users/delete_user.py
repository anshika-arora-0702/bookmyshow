from pydantic import BaseModel, UUID4

class DeleteUserRequest(BaseModel):

    id : UUID4
    deleted_by : UUID4

    