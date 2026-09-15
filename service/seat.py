class SeatService():

    def __init__(self, seatRepo):
        self.seatRepo = seatRepo

    def createSeat(self, new_seat):

        if new_seat.id == None:
            raise ValueError("Error in creating seat id")
        
        if new_seat.audi_id == None:
            raise ValueError("Audi id required")
        
        if new_seat.row_char == None:
            raise ValueError("Row char required")
        
        if new_seat.column_num == None:
            raise ValueError("Column num required")
        
        if new_seat.type == None:
            raise ValueError("Seat type required")
        
        if new_seat.added_by == None:
            raise ValueError("User id required")

        created_seat = self.seatRepo.createSeat(new_seat)
        return created_seat

    def fetchSeat(self, seatId):

        if seatId == None:
            raise ValueError("Seat id required")

        fetched_seat = self.seatRepo.fetchSeat(seatId)

        return fetched_seat

    def deleteSeat(self, seat_to_delete):

        if seat_to_delete.id == None:
            raise ValueError("Seat id required")
        
        if seat_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_seat = self.seatRepo.deleteSeat(seat_to_delete)

        return deleted_seat

    def updateSeat(self, seat_to_update):

        if seat_to_update.id == None:
            raise ValueError("Seat id required")

        if seat_to_update.user_id == None:
            raise ValueError("User id required")

        updated_seat = self.seatRepo.updateSeat(seat_to_update)

        return updated_seat

    def createSeatType(self, new_seat_type):

        if new_seat_type.id == None:
            raise ValueError("Seat Type id required")
        
        if new_seat_type.added_by == None:
            raise ValueError("User id required")
        
        if new_seat_type.name == None:
            raise ValueError("Seat Type name required")

        created_seat_type = self.seatRepo.createSeatType(new_seat_type)
        return created_seat_type

    def fetchSeatType(self, seat_type):

        if seat_type.id == None:
            raise ValueError("Seat Type id required")

        if seat_type.user_id == None:
            raise ValueError("User id required")

        fetched_seat_type = self.seatRepo.fetchSeatType(seat_type)

        return fetched_seat_type

#if we delete what will happen to existing records ??? -> if none of the seats uses it, it will be deleted else db will throw an error

    def deleteSeatType(self, seat_type_to_delete):

        if seat_type_to_delete.id == None:
            raise ValueError("Seat Type id required")
        
        if seat_type_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_seat_type = self.seatRepo.deleteSeatType(seat_type_to_delete)

        return deleted_seat_type

    def updateSeatType(self, seat_type_to_update):

        if seat_type_to_update.id == None:
            raise ValueError("Seat Type id required")

        if seat_type_to_update.user_id == None:
            raise ValueError("User id required")

        updated_seat_type = self.seatRepo.updateSeatType(seat_type_to_update)

        return updated_seat_type