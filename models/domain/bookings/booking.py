import utils

class Booking:

    def __init__(self, id, user_id, payment_id, payment_mode, status,time, seats):

        if id == None:
            self.id = utils.getRandomId()

        else:
            self.id = id

        self.user_id = user_id
        self.payment_id = payment_id
        self.payment_mode = payment_mode
        self.status = status
        self.time = time
        self.seats = seats

    def __str__(self):
        return f"{self.id} : Booking Status {self.status} "