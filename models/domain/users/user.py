import utils.getId as getId

class User:

    def __init__(self, id, first_name, last_name, role, phone, email, dob, password):

        if id == None:
            self.id = getId.getRandomId()

        else:
            self.id = id

        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone = phone
        self.email = email
        self.dob = dob
        self.password = password

    def __str__(self):
        return f"{self.id} : {self.first_name} {self.last_name}"