from pydantic import UUID4

class MovieException(Exception):
    pass

class MovieAlreadyExistsException(MovieException):
    
    def __init__(self):
        super().__init__(f"Movie Already Exists")