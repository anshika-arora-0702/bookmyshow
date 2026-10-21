from models.domain.bookings.booking import Booking as BookingDomain
from models.domain.payments.payment import Payment as PaymentDomain
from models.database.payments.payment_status import PaymentStatus
from models.requests.bookings.cancel_booking import CancelBookingRequest

import utils.getId as getId

from repo.booking import BookingRepo
from service.payment import PaymentService
class BookingService():

    def __init__(self, bookingRepo : BookingRepo, paymentService : PaymentService, db_session):
        self.bookingRepo = bookingRepo
        self.paymentService = paymentService
        self.db_session = db_session

    def _validate_booking(self, new_booking:BookingDomain):

        if new_booking.id == None:
            raise ValueError("Error in creating Booking id")
        
        if new_booking.user_id == None:
            raise ValueError("User id required")
        
        if new_booking.show_id == None:
            raise ValueError("Show id required")        

        if new_booking.seat_ids == None:
            raise ValueError("At least one seat is required")

        if new_booking.payment_id == None:
            raise ValueError("Payment not done")

    def createBooking(self, new_booking:BookingDomain, payment:PaymentDomain):

        self._validate_booking(new_booking)

        with self.db_session.begin():
            created_payment = self.paymentService.createPendingPayment(payment)
            created_booking = self.bookingRepo.createPendingBooking(new_booking)
            self.bookingRepo.reserveSeats(show_id = created_booking.show_id,
                                           seat_ids = created_booking.seat_ids,
                                           booking_id = created_booking.id)

        payment_status = self.paymentService.processPayment(created_payment, created_booking.user_id)

        with self.db_session.begin():

            if payment_status == PaymentStatus.SUCCESSFUL :
                self.bookingRepo.confirmBooking(created_booking.id)
                self.paymentService.markSuccessful(payment.id)
            else:
                self.bookingRepo.failedAndReleaseSeats(created_booking.id)
                self.paymentService.markFailed(payment.id)

        return created_booking

    def fetchBooking(self, booking_to_fetch):

        if booking_to_fetch.id == None:
            raise ValueError("Booking id required")

        if booking_to_fetch.user_id == None:
            raise ValueError("User id required")

        fetched_booking = self.bookingRepo.fetchBooking(booking_to_fetch)

        return fetched_booking

    def cancelBooking(self, booking_to_cancel: CancelBookingRequest):

        if booking_to_cancel.id == None:
            raise ValueError("Booking id  required")
        
        if booking_to_cancel.user_id == None:
            raise ValueError("User id required")

        booking = self.bookingRepo.fetchBooking(booking_to_cancel.id)

        with self.db_session.begin():
            self.bookingRepo.cancelAndReleaseSeats(booking.id)

        with self.db_session.begin():
            payment_id = booking.payment_id
            payment_status = self.paymentService.cancelPayment(payment_id)
            if payment_status == PaymentStatus.CANCELLED:
                self.paymentService.markCancelled(payment_id)

        cancelled_booking = self.bookingRepo.fetchBooking(booking.id)
        return cancelled_booking

#do we need update booking???
