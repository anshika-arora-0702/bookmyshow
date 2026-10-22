from pydantic import UUID4

class CinemaException(Exception):
    pass

class CinemaAlreadyExistsException(CinemaException):

    def __init__(self):
        super().__init__(f"Cinema Already Exists")

class CinemaNotFoundException(CinemaException):

    def __init__(self, cinema_id:UUID4):
        super().__init__(f"Cinema with id '{cinema_id}' not found")

class CinemaIntegrityException(CinemaException):

    def __init__(self):
        super().__init__(f"Cinema data violates a db constraint")