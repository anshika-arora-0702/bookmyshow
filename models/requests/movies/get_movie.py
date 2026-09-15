from pydantic import BaseModel, Field

class GetMovieRequest(BaseModel):

    id:int = Field(
        min_length= 36,
        max_length= 36
    )
    