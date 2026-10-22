from pydantic import UUID4

class MovieException(Exception):
    pass

class MovieAlreadyExistsException(MovieException):

    def __init__(self):
        super().__init__(f"Movie Already Exists")

class MovieIntegrityException(MovieException):

    def __init__(self):
        super().__init__(f"Movie data violates a db constraint")

class MovieNotFoundException(MovieException):

    def __init__(self, movie_id:str):
        self.movie_id = movie_id
        super().__init__(f"Movie with id '{movie_id}' not found")
