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
        
        if new_booking.payment_mode == None:
            raise ValueError("Payment mode required")
        
        if new_booking.seats == None:
            raise ValueError("Seat selection required")
        
        if new_booking.status == None:
            raise ValueError("Booking status not found")
        
        created_booking = self.BookingRepo.createBooking(new_booking)
        return created_booking

    def fetchBooking(self, bookingId):

        if bookingId == None:
            raise ValueError("Booking id required")

        fetched_booking = self.BookingRepo.fetchBooking(bookingId)

        return fetched_booking

    def cancelBooking(self, booking_to_cancel):

        if booking_to_cancel.id == None:
            raise ValueError("Booking id required")
        
        if booking_to_cancel.user_id == None:
            raise ValueError("User id required")

        cancelled_booking = self.BookingRepo.cancelBooking(booking_to_cancel)

        return cancelled_booking

#do we need update booking???

    def createBookingStatusType(self, new_booking_status_type):

        if new_booking_status_type.id == None:
            raise ValueError("Booking Status Type id required")
        
        if new_booking_status_type.added_by == None:
            raise ValueError("User id required")
        
        if new_booking_status_type.name == None:
            raise ValueError("Booking Status Type name required")

        created_booking_status_type = self.BookingRepo.createBookingStatusType(new_booking_status_type)
        return created_booking_status_type

    def fetchBookingStatusType(self, booking_status_typeId):

        if booking_status_typeId == None:
            raise ValueError("Booking Status Type id required")

        #do we need to verify user here???

        fetched_booking_status_type = self.BookingRepo.fetchBookingStatusType(booking_status_typeId)

        return fetched_booking_status_type

    def deleteBookingStatusType(self, booking_status_type_to_delete):

        if booking_status_type_to_delete.id == None:
            raise ValueError("Booking Type id required")
        
        if booking_status_type_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_booking_status_type = self.BookingRepo.deleteBookingStatusType(booking_status_type_to_delete)

        return deleted_booking_status_type

    def updateBookingStatusType(self, Booking_status_type_to_update):

        if Booking_status_type_to_update.id == None:
            raise ValueError("Booking Status Type id required")

        if Booking_status_type_to_update.user_id == None:
            raise ValueError("User id required")

        updated_booking_status_type = self.BookingRepo.updateBookingStatusType(Booking_status_type_to_update)

        return updated_booking_status_type

