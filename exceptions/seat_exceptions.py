class SeatException(Exception):
    pass

class SeatNotFoundException(SeatException):

    def __init__(self, seat_id:str):
        self.seat_id = seat_id
        super().__init__(f"Seat with id '{seat_id}' not found")

class SeatAlreadyExists(SeatException):

    def __init__(self, seat_id:str):
        self.seat_id = seat_id
        super().__init__(f"Seat with id '{seat_id}' already exists")

class SeatIntegrityException(SeatException):

    def __init__(self):
        super().__init__(f"Seat data violates a db constraint")