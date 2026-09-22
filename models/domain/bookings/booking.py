import utils

class Booking:

    def __init__(self, id, user_id, payment_id, status, seats, requested_time, booking_time):

        if id == None:
            self.id = utils.getRandomId()

        else:
            self.id = id

        self.user_id = user_id
        self.payment_id = payment_id
        self.status = status
        self.seats = seats
        self.requested_time = requested_time
        self.booking_time = booking_time

    def __str__(self):
        return f"{self.id} : Booking Status {self.status} "