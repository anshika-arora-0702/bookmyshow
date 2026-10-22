from pydantic import UUID4

class ShowException(Exception):
    pass

class ShowNotFoundException(ShowException):

    def __init__(self, show_id:UUID4):
        self.show_id = show_id
        super().__init__(f"Show with id '{show_id}' not found")

class ShowAlreadyExists(ShowException):

    def __init__(self, show_id:UUID4):
        self.show_id = show_id
        super().__init__(f"Show with id '{show_id}' already exists")

class ShowIntegrityException(ShowException):

    def __init__(self):
        super().__init__(f"Show data violates a db constraint")
