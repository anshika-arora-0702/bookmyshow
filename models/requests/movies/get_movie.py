from pydantic import BaseModel, UUID4

class GetMovieRequest(BaseModel):

    id: UUID4
    