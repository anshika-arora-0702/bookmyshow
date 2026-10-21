import utils.getId as getId

class Payment:

    def __init__(self, id, amount, status, mode):

        if id == None:
            self.id = getId.getRandomId()

        else:
            self.id = id

        self.amount = amount
        self.status = status
        self.mode = mode

    def __str__(self):
        return f"{self.id} : {self.status}"