from fastapi import Depends
from sqlalchemy.orm import Session

from database import SessionLocal

from repo.audi import AudiRepo
from repo.booking import BookingRepo
from repo.cinema import CinemaRepo
from repo.movie import MovieRepo
from repo.payment import PaymentRepo
from repo.seat import SeatRepo
from repo.show import ShowRepo
from repo.user import UserRepo

from service.audi import AudiService
from service.booking import BookingService
from service.cinema import CinemaService
from service.movie import MovieService
from service.payment import PaymentService
from service.seat import SeatService
from service.show import ShowService
from service.user import UserService

def get_db():
    #SessionLocal is actually session generating factory/class
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

def create_audi_service(db:Session = Depends(get_db)):
    audiRepo = AudiRepo(db)
    return AudiService(audiRepo)

def create_booking_service(db:Session = Depends(get_db)):
    bookingRepo = BookingRepo(db)
    return BookingService(bookingRepo)

def create_cinema_service(db:Session = Depends(get_db)):
    cinemaRepo = CinemaRepo(db)
    return CinemaService(cinemaRepo)

def create_movie_service(db:Session = Depends(get_db)):
    movieRepo = MovieRepo(db)
    return MovieService(movieRepo)

def create_payment_service(db:Session = Depends(get_db)):
    paymentRepo = PaymentRepo(db)
    return PaymentService(paymentRepo)

def create_seat_service(db:Session = Depends(get_db)):
    seatRepo = SeatRepo(db)
    return SeatService(seatRepo)

def create_show_service(db:Session = Depends(get_db)):
    showRepo = ShowRepo(db)
    return ShowService(showRepo)

def create_user_service(db:Session = Depends(get_db)):
    userRepo = UserRepo(db)
    return UserService(userRepo)