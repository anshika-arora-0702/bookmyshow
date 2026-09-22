from pydantic import UUID4

class BookingException(Exception):
    pass

class BookingNotFoundException(BookingException):

    def __init__(self, booking_id:UUID4):
        self.booking_id = booking_id
        super().__init__(f"Booking with id '{booking_id}' not found")

class BookingAlreadyExists(BookingException):

    def __init__(self, booking_id:str):
        self.booking_id = booking_id
        super().__init__(f"Booking with id '{booking_id}' already exists")