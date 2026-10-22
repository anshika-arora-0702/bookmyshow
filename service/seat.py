from utils.row_label import row_label
from utils.row_number import row_number
from utils.getId import getRandomId

from models.domain.seats.seat import Seat as SeatDomain
from models.database.seats.seat_type import SeatType
from models.database.audis.audi import Audi as AudiDB

class SeatService():

    def __init__(self, seatRepo):
        self.seatRepo = seatRepo

    def _validate_seat(self, new_seat, audi_column_count, audi_row_count):

        if new_seat.id == None:
            raise ValueError("Error in creating seat id")
        
        if new_seat.audi_id == None:
            raise ValueError("Audi id required")
        
        if new_seat.row_char == None:
            raise ValueError("Row char required")
        
        if row_number(new_seat.row_char) > audi_row_count:
            raise ValueError("Row char greater than max rows in audi")
        
        if new_seat.column_num == None:
            raise ValueError("Column num required")
        
        if new_seat.column_num > audi_column_count:
            raise ValueError("Column num greater than max column in audi")
        
        if new_seat.type == None:
            raise ValueError("Seat type required")

    def createAudiSeats(self, audi_id, column_count, row_count):
            
            for row_index in range(1,row_count+1):
                row_char = row_label(row_index)

                for column_num in range(1, column_count + 1):
                    seat = SeatDomain(id = getRandomId(),
                                audi_id = audi_id,
                                column_num = column_num,
                                row_char = row_char,
                                type = SeatType.NORMAL,
                                )
                    self.createSeat(seat, column_count, row_count )

    def createSeat(self, new_seat:SeatDomain, audi_column_count, audi_row_count ):
        
        self._validate_seat(new_seat, audi_column_count, audi_row_count)
        created_seat = self.seatRepo.createSeat(new_seat)
        return created_seat

    def fetchAudiSeats(self, audi_id):
        return self.seatRepo.fetchAudiSeats(audi_id)

    def fetchAudiSeatTypes(self, audi_id):
        return self.seatRepo.fetchAudiSeatTypes(audi_id)

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
