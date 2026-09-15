class ShowSeatAvailability:

    def __init__(self, show_id, seat_id, booking_id, availability):

        self.show_id = show_id
        self.seat_id = seat_id
        self.booking_id = booking_id
        self.availability = availability

    def __str__(self):
        return f"Seat {self.seat_id} , Show {self.show_id} : {self.availability}"