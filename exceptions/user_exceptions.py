class UserException(Exception):
    pass

class UnauthorizedException(UserException):

    def __init__(self, resource:str, action:str):
        super().__init__(f"Unauthorized to {action} {resource}")

class UserDoesnotExistException(UserException):

    def __init__(self):
        super().__init__(f"User Doesn't Exist")
class UserAlreadyExistsException(UserException):

    def __init__(self):
        super().__init__(f"User Already Exists")