from fastapi import FastAPI

from models.database.audis import audi
from models.database.audis import audi_type
from models.database.users import user
from models.database.cinemas import cinema

from database import SessionLocal, Engine

from routers.audi import createAudiRouter
app = FastAPI()


audi.Base.metadata.create_all(bind=Engine)

app.include_router(
    createAudiRouter(),
    prefix = "/audi",
    tags = ["Audi Management"]
)