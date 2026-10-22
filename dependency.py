from fastapi import Depends
from sqlalchemy.orm import Session

from database import SessionLocal

from repo.audi import AudiRepo
from repo.booking import BookingRepo
from repo.cinema import CinemaRepo
from repo.city import CityRepo
from repo.movie import MovieRepo
from repo.payment import PaymentRepo
from repo.seat import SeatRepo
from repo.show import ShowRepo
from repo.user import UserRepo

from service.audi import AudiService
from service.booking import BookingService
from service.cinema import CinemaService
from service.city import CityService
from service.movie import MovieService
from service.payment import PaymentService
from service.seat import SeatService
from service.show import ShowService
from service.user import UserService
from service.payment_provider import FakePaymentProvider

def get_db():
    #SessionLocal is actually session generating factory/class
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

def create_user_service(db:Session = Depends(get_db)):
    userRepo = UserRepo(db)
    return UserService(userRepo)




def create_payment_service(db:Session = Depends(get_db)):
    paymentRepo = PaymentRepo(db)
    return PaymentService(paymentRepo, FakePaymentProvider() )

def create_booking_service(db:Session = Depends(get_db),
                           payment_service : PaymentService = Depends(create_payment_service)):
    bookingRepo = BookingRepo(db)
    return BookingService(bookingRepo, payment_service, db)

def create_cinema_service(db:Session = Depends(get_db)):
    cinemaRepo = CinemaRepo(db)
    return CinemaService(cinemaRepo)

def create_city_service(db:Session = Depends(get_db)):
    cityRepo = CityRepo(db)
    return CityService(cityRepo)

def create_movie_service(db:Session = Depends(get_db)):
    movieRepo = MovieRepo(db)
    return MovieService(movieRepo)

def create_seat_service(db:Session = Depends(get_db)):
    seatRepo = SeatRepo(db)
    return SeatService(seatRepo)

def create_audi_service(db:Session = Depends(get_db), 
                        seat_service : SeatService = Depends(create_seat_service),
                        user_service : UserService = Depends(create_user_service),
                        cinema_service: CinemaService = Depends(create_cinema_service)):
    audiRepo = AudiRepo(db)
    return AudiService(audiRepo, seat_service, user_service, cinema_service, db)

def create_show_service(db:Session = Depends(get_db),
                        seat_service: SeatService = Depends(create_seat_service),
                        user_service : UserService = Depends(create_user_service),
                        audi_service: AudiService = Depends(create_audi_service),
                        movie_service: MovieService = Depends(create_movie_service)):
    showRepo = ShowRepo(db)
    return ShowService(showRepo, seat_service, user_service, audi_service,movie_service, db)

