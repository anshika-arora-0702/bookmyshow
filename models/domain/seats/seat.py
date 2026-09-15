import utils

class Seat:

    def __init__(self, id, audi_id, column_num, row_char, type, added_by):

        if id == None:
            self.id = utils.getRandomId()

        else:
            self.id = id

        self.audi_id = audi_id
        self.column_num = column_num
        self.row_char = row_char
        self.type = type
        self.added_by = added_by

    def __str__(self):
        return f"{self.id} : {self.audi_id}"