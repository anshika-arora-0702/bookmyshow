import utils.getId as getId

class Cinema:

    def __init__(self, id, added_by, name, address, city):

        self.id = id
        self.added_by = added_by
        self.name = name
        self.address = address
        self.city = city


    def __str__(self):
        return f"{self.id} : {self.name}"