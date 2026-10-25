from models.domain.shows.show import Show
from models.domain.movies.movie import Movie
from service.seat import SeatService
from service.user import UserService
from service.audi import AudiService
from service.movie import MovieService
from repo.show import ShowRepo

from datetime import timedelta

from decimal import Decimal

from exceptions import user_exceptions
from exceptions import show_exceptions

from sqlalchemy.exc import IntegrityError

class ShowService():

    def __init__(self, showRepo:ShowRepo, seatService: SeatService, userService:UserService, audiService: AudiService,movieService: MovieService, db_session):
        self.showRepo = showRepo
        self.db_session = db_session
        self.seatService = seatService
        self.userService = userService
        self.audiService = audiService
        self.movieService = movieService

    def _validate_show(self, new_show):

        if new_show.id == None:
            raise ValueError("Error in creating Show id")
        
        if new_show.added_by == None:
            raise ValueError("User id required")
        
        if new_show.audi_id == None:
            raise ValueError("Audi id required")
        
        if new_show.movie_id == None:
            raise ValueError("Movie id required")
        
        if new_show.start_time == None:
            raise ValueError("Start time required")
        
        if new_show.price == None:
            raise ValueError("Price required")

    def _fetch_audi(self, audi_id):
        return self.audiService._fetch_audi(audi_id)

    def _fetch_movie(self,movie_id):
        return self.movieService._fetch_movie(movie_id)

    def _is_superadmin(self, user_id):
        return self.userService._is_superadmin(user_id)

    def _validate_price(self, audi_id, price):
            seat_types = set(self.seatService.fetchAudiSeatTypes(audi_id))
            provided_types = set(price.keys())
            missing_prices = seat_types - provided_types

            if missing_prices:
                raise ValueError(f"Missing prices for seat types: {missing_prices}")

    def _validate_time(self, proposed_start_time, audi_id, movie:Movie):
        if proposed_start_time.date() < movie.release_date:
            raise ValueError("Cannot schedule a show before the movie's release date")

        if movie.runtime_in_sec <= 0:
            raise ValueError("Movie runtime must be set greater than zero")
        proposed_end_time = proposed_start_time + timedelta(seconds=movie.runtime_in_sec)
        self.showRepo._validate_time(audi_id, proposed_start_time, proposed_end_time)
        return proposed_end_time

    def _calculate_show_seats_price(self,show_id, seat_ids):

        if show_id is None:
            raise ValueError("No show provided")
        if seat_ids is None:
            raise ValueError("No seats provided")

        seat_ids_types : dict = self.seatService.seats_type(seat_ids)

        price_dict = self.showRepo._calculate_show_seats_price(show_id, seat_ids)

        price = Decimal("0.00")

        for seat_id in seat_ids:
            seat_type = seat_ids_types[seat_id]
            price = price + Decimal(str(price_dict[seat_type.value]))

            '''Since seat_type is SeatType Enum but in price_dict(stored in JSON format), keys are strings not SeatType Enum
            .value will convert enums to strings to look in dictionary'''
            
        return price


    def reserveSeats(self, show_id,seat_ids,booking_id):
        return self.showRepo.reserveSeats(show_id,seat_ids,booking_id)

    def releaseSeats(self,booking_id, show_id, seat_ids):
        return self.showRepo.releaseSeats(booking_id, show_id,seat_ids)
        


    # def createShow(self, new_show: Show):

    #     self._validate_show(new_show)

    #     try:

    #         with self.db_session.begin():
    #             audi = self._fetch_audi(new_show.audi_id)
    #             movie = self._fetch_movie(new_show.movie_id)

    #             if audi.user_id != new_show.added_by and not(self._is_superadmin(new_show.added_by)):
    #                 raise user_exceptions.UnauthorizedException("Show" , "create")
                
    #             self._validate_price(audi.id, new_show.price)
    #             end_time = self._validate_time(new_show.start_time,new_show.audi_id, movie)
    #             created_show = self.showRepo.createShow(new_show, end_time)
    #             seat_list = self.seatService.fetchAudiSeats(created_show.audi_id)
    #             self.showRepo.createShowSeats(created_show.id, seat_list)

    #         return created_show
        
    #     except IntegrityError as e:
    #         raise show_exceptions.ShowIntegrityException() from e

    # def fetchShow(self, showId):

    #     if showId == None:
    #         raise ValueError("Show id required")

    #     fetched_show = self.ShowRepo.fetchShow(showId)

    #     return fetched_show

    # def deleteShow(self, show_to_delete):

    #     if show_to_delete.id == None:
    #         raise ValueError("Show id required")
        
    #     if show_to_delete.deleted_by_id == None:
    #         raise ValueError("Deleted by id required")

    #     deleted_show = self.ShowRepo.deleteShow(show_to_delete)

    #     return deleted_show

    # def updateShow(self, show_to_update):

    #     if show_to_update.id == None:
    #         raise ValueError("Show id required")

    #     if show_to_update.updates_by_id == None:
    #         raise ValueError("Updates by id is required")

    #     updated_show = self.showRepo.updateShow(show_to_update)

    #     return updated_show

    # def fetchShowSeatAvailability(self, showId):

    #     if showId == None:
    #         raise ValueError("Show id required")

    #     fetched_show_seat_availability = self.ShowRepo.fetchShowSeatAvailability(showId)

    #     return fetched_show_seat_availability

    # #when a booking is made or cancelled
    # def updateShowSeatAvailability(self, show_seat_availability_to_update):

    #     if show_seat_availability_to_update.show_id == None:
    #         raise ValueError("Show id required")
        
    #     if show_seat_availability_to_update.seats == None:
    #         raise ValueError("Seats required")
        
    #     if show_seat_availability_to_update.booking_id == None:
    #         raise ValueError("Booking id required")

    #     updated_show_seat_availability = self.ShowRepo.updateShowSeatAvailability(show_seat_availability_to_update)

    #     return updated_show_seat_availability


