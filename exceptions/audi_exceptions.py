class AudiException(Exception):
    pass

class AudiNotFoundException(AudiException):

    def __init__(self, audi_id:str):
        self.audi_id = audi_id
        super().__init__(f"Audi with id '{audi_id}' not found")

class AudiAlreadyExists(AudiException):

    def __init__(self, audi_id:str):
        self.audi_id = audi_id
        super().__init__(f"Audi with id '{audi_id}' already exists")