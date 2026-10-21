from fastapi import FastAPI

from models.database.audis import audi
from models.database.users import user
from models.database.cinemas import cinema
from models.database.bookings import booking

from database import SessionLocal, Engine

from routers.audi import createAudiRouter
from routers.booking import createBookingRouter
from routers.user import createUserRouter
from routers.cinema import createCinemaRouter
from routers.city import createCityRouter
from routers.movie import createMovieRouter


app = FastAPI()

from models.database.base import Base
Base.metadata.create_all(bind=Engine)

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

app.include_router(
    createUserRouter(),
    prefix = "/user",
    tags = ["User Management"]
)

app.include_router(
    createCinemaRouter(),
    prefix="/cinema",
    tags=["Cinema Management"]
)

app.include_router(
    createCityRouter(),
    prefix="/city",
    tags=["City Management"]
)

app.include_router(
    createMovieRouter(),
    prefix ="/movie",
    tags = ["Movie Management"]
)