import utils

class User:

    def __init__(self, id, first_name, last_name, role, phone, email, dob):

        if id == None:
            self.id = utils.getRandomId()

        else:
            self.id = id

        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone = phone
        self.email = email
        self.dob = dob

    def __str__(self):
        return f"{self.id} : {self.first_name} {self.last_name}"