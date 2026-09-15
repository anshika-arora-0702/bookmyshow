import utils

class Audi:

    def __init__(self, id, added_by, cinema_id, screen_num, row_count, column_count, type):

        self.id = id
        self.added_by = added_by
        self.cinema_id = cinema_id
        self.screen_num = screen_num
        self.row_count = row_count
        self.column_count = column_count
        self.type = type

    def __str__(self):
        return f"{self.id} : Cinema {self.cinema_id} Screen {self.screen_num} "