class UserException(Exception):
    pass

class UnauthorizedException(UserException):

    def __init__(self, resource:str, action:str):
        super().__init__(f"Unauthorized to {action} {resource}")

class UserDoesnotExistException(UserException):

    def __init__(self, user_id):
        super().__init__(f"User with id {user_id} doesn't Exist")

class UserAlreadyExistsException(UserException):

    def __init__(self):
        super().__init__(f"User Already Exists")

class FieldChangeNotAllowed(UserException):

    def __init__(self, field):
        super().__init__(f"{field} cannot be changed")

class UserContactAlreadyExistsException(UserException):
    def __init__(self):
        super().__init__("Phone number or email is already in use")
