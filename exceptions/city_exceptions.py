from pydantic import UUID4

class CityException(Exception):
    pass

class CityAlreadyExistsException(CityException):

    def __init__(self):
        super().__init__(f"City Already Exists")