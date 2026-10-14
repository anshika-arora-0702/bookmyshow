from pydantic import UUID4 

from models.domain.bookings.booking import Booking as BookingDomain
from models.database.bookings.booking import Booking as BookingDB
from models.database.bookings.booking_status import BookingStatus
from models.database.shows.show_seat_availability import ShowSeatAvailability

from models.database.shows.show import Show as ShowDB
from models.database.users.user import User as UserDB

from exceptions import booking_exceptions 
from exceptions import user_exceptions 
from exceptions import show_exceptions 
from exceptions import user_exceptions 

from datetime import datetime,timezone

class BookingRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _validate_booking(self, booking: BookingDomain):

        if self.db_session.get(BookingDB,booking.id) != None:
            raise booking_exceptions.BookingAlreadyExists(booking.id)

        show = self.db_session.get(ShowDB, booking.show_id)

        if show == None:
            raise show_exceptions.ShowNotFoundException()

        user = self.db_session.get(UserDB, booking.user_id)

        if user == None:
            raise user_exceptions.UserDoesnotExistException()

    def _booking_to_db(self,booking:BookingDomain) -> BookingDB:

        return BookingDB(id = booking.id, 
                      user_id = booking.user_id, 
                      payment_id = booking.payment_id,  
                      show_id = booking.show_id,
                      seats_ids = booking.seat_ids, 
                      status = booking.status,
                      requested_time = booking.requested_time,
                      booking_time = datetime.now(timezone.utc),
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )

    def _booking_to_domain(self,booking:BookingDB) -> BookingDomain:

        return BookingDomain(id = booking.id, 
                      user_id = booking.user_id, 
                      payment_id =  booking.payment_id,
                      seats_ids = booking.seat_ids, 
                      status = booking.status,
                      requested_time= booking.requested_time,
                      booking_time = booking.booking_time
                      )


    def createPendingBooking(self, booking_to_create_domain:BookingDomain) -> BookingDomain:

        self._validate_booking(booking_to_create_domain)


        try:
            booking_db = self._booking_to_db(booking_to_create_domain)
            self.db_session.add(booking_db)
            self.db_session.commit()
            self.db_session.refresh(booking_db)
            return self._booking_to_domain(booking_db)

        except Exception :
            self.db_session.rollback()
            raise booking_exceptions()

    def reserveSeats(self, show_id,seat_ids,booking_id):
        try:
            for seat_id in seat_ids:
                show_seat = self.db_session.get(ShowSeatAvailability, (show_id, seat_id))

                if show_seat is not None and show_seat.availability:
                    show_seat.availability = False
                    show_seat.booking_id = booking_id
                    show_seat.updated_at = datetime.now(timezone.utc)

                else:
                    raise booking_exceptions()

            self.db_session.commit()


        except Exception:
            self.db_session.rollback()
            raise booking_exceptions()

    def confirmBooking(self, booking_id):
        try:
            booking = self.db_session.get(BookingDB, booking_id )
            booking.status = BookingStatus.BOOKED
            booking.booking_time = datetime.now(timezone.utc)
            booking.updated_at = datetime.now(timezone.utc)
            self.db_session.commit()

        except:
            self.db_session.rollback()
            raise booking_exceptions()
   
    def failedAndReleaseSeats(self, booking_id):

        try:
            booking = self.db_session.get(BookingDB, booking_id )
            booking.status = BookingStatus.FAILED

            for seat_id in booking.seat_ids:
                show_seat = self.db_session.get(ShowSeatAvailability, (booking.show_id, seat_id))
                
                show_seat.availability = True
                show_seat.booking_id = None
                show_seat.updated_at = datetime.now(timezone.utc)

            self.db_session.commit()

        except:
            self.db_session.rollback()
            raise booking_exceptions()

    def cancelAndReleaseSeats(self, booking_id):

        try:
            booking = self.db_session.get(BookingDB, booking_id )
            booking.status = BookingStatus.CANCELLED

            for seat_id in booking.seat_ids:
                show_seat = self.db_session.get(ShowSeatAvailability, (booking.show_id, seat_id))
                
                show_seat.availability = True
                show_seat.booking_id = None
                show_seat.updated_at = datetime.now(timezone.utc)

            self.db_session.commit()

        except:
            self.db_session.rollback()
            raise booking_exceptions()

    def fetchBooking(self, booking_to_fetch) -> BookingDomain:

        fetched_booking_db = self.db_session.get(BookingDB, booking_to_fetch.id)

        if fetched_booking_db == None:
            raise booking_exceptions.BookingNotFoundException(booking_to_fetch.id)

        user = self.db_session.get(UserDB,booking_to_fetch.user_id)

        if not (
            (user.role == 'SUPER_ADMIN') or 
            (user.role == 'ADMIN') or
            (fetched_booking_db.user_id == user.user_id)
            ):
            raise user_exceptions.UnauthorizedException("Booking", "fetch")

        return self._booking_to_domain(fetched_booking_db)


           


