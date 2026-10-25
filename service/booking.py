from decimal import Decimal

from models.domain.bookings.booking import Booking as BookingDomain
from models.domain.payments.payment import Payment as PaymentDomain
from models.database.payments.payment_status import PaymentStatus
from models.database.bookings.booking_status import BookingStatus
from models.requests.bookings.cancel_booking import CancelBookingRequest

import utils.getId as getId

from repo.booking import BookingRepo
from service.payment import PaymentService
from service.user import UserService
from service.show import ShowService

from exceptions import booking_exceptions
class BookingService():

    def __init__(self, bookingRepo : BookingRepo, paymentService : PaymentService, userService:UserService ,showService:ShowService, db_session):
        self.bookingRepo = bookingRepo
        self.paymentService = paymentService
        self.db_session = db_session
        self.userService = userService
        self.showService = showService

    def _validate_booking(self, new_booking:BookingDomain):

        if new_booking.id == None:
            raise ValueError("Error in creating Booking id")
        
        if new_booking.user_id == None:
            raise ValueError("User id required")
        
        if new_booking.show_id == None:
            raise ValueError("Show id required")        

        if not new_booking.seat_ids:
            raise ValueError("At least one seat is required")

    def createBooking(self, new_booking:BookingDomain, payment_mode):

        self._validate_booking(new_booking)

        try:

            with self.db_session.begin():
                self.userService._is_valid_user(new_booking.user_id)
                price = self.showService._calculate_show_seats_price(new_booking.show_id, new_booking.seat_ids)

                payment = PaymentDomain(id = getId.getRandomId(), 
                                        amount=price,
                                        status=PaymentStatus.PENDING,
                                        mode=payment_mode )

                new_booking.payment_id = payment.id
                created_payment: PaymentDomain = self.paymentService.createPendingPayment(payment)
                created_booking: BookingDomain = self.bookingRepo.createPendingBooking(new_booking)
                self.showService.reserveSeats(show_id = created_booking.show_id,
                                            seat_ids = created_booking.seat_ids,
                                            booking_id = created_booking.id)

            payment_status = self.paymentService.processPayment(created_payment, created_booking.user_id)

            with self.db_session.begin():

                if payment_status == PaymentStatus.SUCCESSFUL :
                    self.bookingRepo.markBookingConfirmed(created_booking.id)
                    self.paymentService.markSuccessful(payment.id)
                    created_booking.status = BookingStatus.BOOKED

                elif payment_status == PaymentStatus.FAILED :
                    self.bookingRepo.markBookingFailed(created_booking.id)
                    self.showService.releaseSeats(created_booking.id,created_booking.show_id,created_booking.seat_ids)
                    self.paymentService.markFailed(payment.id)
                    created_booking.status= BookingStatus.FAILED

                elif payment_status == PaymentStatus.UNKNOWN:
                    self.paymentService.markUnknown(payment.id)
                    created_booking.status = BookingStatus.PENDING

                else:
                    raise ValueError(f"Unexpected payment status: {payment_status}")

            return created_booking

        except Exception as e:
            raise Exception from e


    # def fetchBooking(self, booking_to_fetch):

    #     if booking_to_fetch.id == None:
    #         raise ValueError("Booking id required")

    #     if booking_to_fetch.user_id == None:
    #         raise ValueError("User id required")

    #     fetched_booking = self.bookingRepo.fetchBooking(booking_to_fetch)

    #     return fetched_booking

    # def cancelBooking(self, booking_to_cancel: CancelBookingRequest):

    #     if booking_to_cancel.id == None:
    #         raise ValueError("Booking id  required")
        
    #     if booking_to_cancel.user_id == None:
    #         raise ValueError("User id required")

    #     booking = self.bookingRepo.fetchBooking(booking_to_cancel.id)

    #     with self.db_session.begin():
    #         self.bookingRepo.cancelAndReleaseSeats(booking.id)

    #     with self.db_session.begin():
    #         payment_id = booking.payment_id
    #         payment_status = self.paymentService.cancelPayment(payment_id)
    #         if payment_status == PaymentStatus.CANCELLED:
    #             self.paymentService.markCancelled(payment_id)

    #     cancelled_booking = self.bookingRepo.fetchBooking(booking.id)
    #     return cancelled_booking

#do we need update booking???
