from pydantic import BaseModel, UUID4

class UpdateRoleRequest(BaseModel):
    updated_by : UUID4
    id : UUID4
    