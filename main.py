from fastapi import FastAPI

from models.database.audis import audi
from models.database.users import user
from models.database.cinemas import cinema
from models.database.bookings import booking

from database import SessionLocal, Engine

from routers.audi import createAudiRouter
from routers.booking import createBookingRouter
app = FastAPI()


audi.Base.metadata.create_all(bind=Engine)
booking.Base.metadata.create_all(bind = Engine)

app.include_router(
    createAudiRouter(),
    prefix = "/audi",
    tags = ["Audi Management"]
)

app.include_router(
    createBookingRouter(),
    prefix = "/booking",
    tags = ["Booking Management"]
)