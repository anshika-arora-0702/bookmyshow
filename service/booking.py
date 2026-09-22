class BookingService():

    def __init__(self, bookingRepo):
        self.bookingRepo = bookingRepo

    def createBooking(self, new_booking):

        if new_booking.id == None:
            raise ValueError("Error in creating Booking id")
        
        if new_booking.user_id == None:
            raise ValueError("User id required")
        
        if new_booking.payment_id == None:
            raise ValueError("Payment id required")
        
        if new_booking.seats == None:
            raise ValueError("Seat selection required")
        
        created_booking = self.bookingRepo.createBooking(new_booking)
        return created_booking

    def fetchBooking(self, booking_to_fetch):

        if booking_to_fetch.id == None:
            raise ValueError("Booking id required")

        if booking_to_fetch.user_id == None:
            raise ValueError("User id required")

        fetched_booking = self.bookingRepo.fetchBooking(booking_to_fetch)

        return fetched_booking

    def cancelBooking(self, booking_to_cancel):

        if booking_to_cancel.id == None:
            raise ValueError("Booking id required")
        
        if booking_to_cancel.user_id == None:
            raise ValueError("User id required")

        cancelled_booking = self.BookingRepo.cancelBooking(booking_to_cancel)

        return cancelled_booking

#do we need update booking???
