class AudiType:

    def __init__(self, id, added_by, name):

        self.id = id
        self.added_by = added_by
        self.name = name

    def __str__(self):
        return f"{self.id} : {self.name}"