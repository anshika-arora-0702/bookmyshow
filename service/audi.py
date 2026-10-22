from repo.audi import AudiRepo
from service.seat import SeatService
from service.user import UserService
from service.cinema import CinemaService

from models.domain.audis.audi import Audi
from models.domain.seats.seat import Seat

from exceptions import user_exceptions

class AudiService():

    def __init__(self, audiRepo:AudiRepo, seatService:SeatService, userService: UserService, cinemaService: CinemaService, db_session):
        self.audiRepo = audiRepo
        self.seatService = seatService
        self.db_session = db_session
        self.userService = userService
        self.cinemaService = cinemaService

    def _fetch_audi(self, audi_id):
        return self.audiRepo._fetch_audi(audi_id)

    def _fetch_cinema(self, cinema_id):
        return self.cinemaService._fetch_cinema(cinema_id)

    def _is_admin(self, user_id):
        return self.userService._is_admin(user_id)

    def _validate_audi(self, new_audi:Audi):

        if new_audi.id == None:
            raise ValueError("Error in creating audi id")
        
        if new_audi.user_id == None:
            raise ValueError("User id required")
        
        if new_audi.cinema_id == None:
            raise ValueError("Cinema id required")
        
        if new_audi.row_count == None:
            raise ValueError("Row count required")
        
        if new_audi.column_count == None:
            raise ValueError("Column count required")
        
        if new_audi.type == None:
            raise ValueError("Audi type required")
        
        if new_audi.screen_num == None:
            raise ValueError("Screen number required")

    def createAudi(self, new_audi:Audi):

        self._validate_audi(new_audi)

        ''' Whu cinema before with block giving error as  {
                "detail": "A transaction is already begun on this Session."
                }
        cinema = self._fetch_cinema(new_audi.cinema_id)
        with self.db_session.begin():
            
            if cinema.added_by != new_audi.user_id and not(self._is_admin(new_audi.user_id)):
                raise user_exceptions.UnauthorizedException("Audi" , "create")'''
        
        with self.db_session.begin():
            cinema = self._fetch_cinema(new_audi.cinema_id)
            if cinema.added_by != new_audi.user_id and not(self._is_admin(new_audi.user_id)):
                raise user_exceptions.UnauthorizedException("Audi" , "create")

            created_audi = self.audiRepo.createAudi(new_audi)
            self.seatService.createAudiSeats(created_audi.id, created_audi.column_count, created_audi.row_count)
            
        return created_audi

    def createSeat(self,new_seat:Seat, user_id):
        audi = self._fetch_audi(new_seat.audi_id)
        if audi.user_id != user_id and not(self._is_admin(user_id)):
            raise user_exceptions.UnauthorizedException("Seat" , "create")

        return self.seatService.createSeat(new_seat, user_id)
    

    def fetchAudi(self, audi_to_fetch):

        if audi_to_fetch.id == None:
            raise ValueError("Audi id required")

        if audi_to_fetch.user_id == None:
            raise ValueError("User id required")

        fetched_audi = self.audiRepo.fetchAudi(audi_to_fetch)

        return fetched_audi

    # def deleteAudi(self, audi_to_delete):

    #     if audi_to_delete.id == None:
    #         raise ValueError("Audi id required")
        
    #     if audi_to_delete.user_id == None:
    #         raise ValueError("User id required")

    #     deleted_audi = self.audiRepo.deleteAudi(audi_to_delete)

    #     return deleted_audi

    # def updateAudi(self, audi_to_update):

    #     if audi_to_update.id == None:
    #         raise ValueError("Audi id required")

    #     if audi_to_update.user_id == None:
    #         raise ValueError("User id required")

    #     updated_audi = self.audiRepo.updateAudi(audi_to_update)

    #     return updated_audi
