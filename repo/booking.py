from models.domain.bookings.booking import Booking as BookingDomain
from models.database.bookings.booking import Booking as BookingDB
from models.database.bookings.booking_status import BookingStatus
from models.database.shows.show_seat_availability import ShowSeatAvailability

from models.database.users.user import User as UserDB

from exceptions import booking_exceptions as e
from exceptions import auth_exceptions as ae

from datetime import datetime,timezone

class BookingRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _booking_to_db(self,booking:BookingDomain) -> BookingDB:

        return BookingDB(id = booking.id, 
                      user_id = booking.user_id, 
                      payment_id = booking.payment_id,  
                      seats = booking.seats, 
                      status = BookingStatus.BOOKED,
                      requested_time = booking.requested_time,
                      booking_time = booking.booking_time,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )

    def _booking_to_domain(self,booking:BookingDB) -> BookingDomain:

        return BookingDomain(id = booking.id, 
                      user_id = booking.user_id, 
                      payment_id = booking.payment_id,  
                      seats = booking.seats, 
                      status = BookingStatus.BOOKED,
                      requested_time= booking.requested_time,
                      booking_time = datetime.now(timezone.utc),
                      created_at = datetime.now(timezone.utc),
                      updated_at =datetime.now(timezone.utc)
                      )

    def createBooking(self, booking_to_create_domain:BookingDomain) -> BookingDomain:

        if self.db_session.get(BookingDB,booking_to_create_domain.id) != None:
            raise e.BookingAlreadyExists(booking_to_create_domain.id)

        user = self.db_session.get(UserDB,booking_to_create_domain.user_id)

        if user == None:
            raise ae.UserDoesnotExistException()

        try:
            show_seat_list = booking_to_create_domain.seats
            for seat in show_seat_list:
                seat_db = self.db_session.get(ShowSeatAvailability, seat.id )

            booking_to_create_db = self._booking_to_db(booking_to_create_domain)
            self.db_session.add(booking_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(booking_to_create_db)
            return self._booking_to_domain(booking_to_create_db)

        except Exception :
            self.db_session.rollback()
            raise e.AudiException()

    def fetchBooking(self, booking_to_fetch) -> BookingDomain:

        fetched_booking_db = self.db_session.get(BookingDB, booking_to_fetch.id)

        if fetched_booking_db == None:
            raise e.BookingNotFoundException(booking_to_fetch.id)


        user = self.db_session.get(UserDB,booking_to_fetch.user_id)

        if not (
            (user.role == 'SUPER_ADMIN') or 
            (user.role == 'ADMIN') or
            (fetched_booking_db.added_by == booking_to_fetch.user_id)
            ):
            raise ae.UnauthorizedException("Booking", "fetch")

        return self._booking_to_domain(fetched_booking_db)

    def cancelBooking(self, booking_to_cancel):

        booking_to_cancel_db = self.db_session.get(BookingDB, booking_to_cancel.id)

        if booking_to_cancel_db == None:
            raise e.BookingNotFoundException(booking_to_cancel.id)

        user = self.db_session.get(UserDB,booking_to_cancel.user_id)

        if not (
            (user.role == 'SUPER_ADMIN') or  
            (booking_to_cancel_db.added_by == user.id)
            ):
            raise ae.UnauthorizedException("Booking", "cancel")
        
        try:
            booking_to_cancel_db.status = BookingStatus.CANCELLED
            booking_to_cancel_db.updated_at = datetime.now(timezone.utc)
            self.db_session.commit()
            self.db_session.refresh(booking_to_cancel_db)
            return self._audi_to_domain(booking_to_cancel_db)

        except Exception :
            self.db_session.rollback()
            raise e.BookingException()
