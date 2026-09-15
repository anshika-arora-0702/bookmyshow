import utils

class Show:

    def __init__(self, id, added_by, audi_id, movie_id, start_time, price):

        self.id = id
        self.added_by = added_by
        self.audi_id = audi_id
        self.movie_id = movie_id
        self.start_time = start_time
        self.price = price

    def __str__(self):
        return f"{self.id} : Audi {self.audi_id} Movie {self.movie_id}"