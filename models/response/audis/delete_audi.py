from pydantic import BaseModel, ConfigDict, UUID4

class DeleteAudiResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:UUID4
    