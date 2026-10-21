from pydantic import UUID4

class CinemaException(Exception):
    pass

class CinemaAlreadyExistsException(CinemaException):

    def __init__(self):
        super().__init__(f"Cinema Already Exists")

class CinemaIntegrityException(CinemaException):

    def __init__(self):
        super().__init__(f"Cinema data violates a db constraint")