from pydantic import BaseModel, ConfigDict
from datetime  import date

class GetMovieResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    name:str
    poster:str | None = None
    runtime_in_sec:int | None = None
    release_date:date | None = None
    details:str | None = None