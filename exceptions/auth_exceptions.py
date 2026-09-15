class AuthException(Exception):
    pass

class UnauthorizedException(AuthException):

    def __init__(self, resource:str, action:str):
        super().__init__(f"Unauthorized to {action} {resource}")

class UserDoesnotExistException(AuthException):

    def __init__(self):
        super().__init__(f"User Doesn't Exist")