class SeatType:

    def __init__(self, id, name, added_by):

        self.id = id
        self.name = name
        self.added_by = added_by

    def __str__(self):
        return f"{self.id} : {self.name}"