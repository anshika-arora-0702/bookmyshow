from pydantic import BaseModel, Field

class DeleteMovieRequest(BaseModel):

    id:int = Field(
        min_length= 36,
        max_length= 36
    )

    user_id:int = Field(
        min_length= 36,
        max_length= 36
    )