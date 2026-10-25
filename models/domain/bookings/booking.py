from models.database.bookings.booking_status import BookingStatus
import utils.getId as getId

class Booking:

    def __init__(self, 
                 id, 
                 user_id, 
                 payment_id, 
                 seat_ids, 
                 show_id,
                 status = BookingStatus.PENDING
                 ):

        self.id = id or getId.getRandomId()
        self.user_id = user_id
        self.payment_id = payment_id
        self.seat_ids = seat_ids
        self.show_id = show_id
        self.status = status

    def __str__(self):
        return f"{self.id} : Booking Status {self.status} "