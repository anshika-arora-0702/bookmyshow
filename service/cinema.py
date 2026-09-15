class CinemaService():

    def __init__(self, cinemaRepo):
        self.cinemaRepo = cinemaRepo

    def createCinema(self, new_cinema):

        if new_cinema.id == None:
            raise ValueError("Error in creating cinema id")
        
        if new_cinema.added_by == None:
            raise ValueError("User id required")
        
        if new_cinema.name == None:
            raise ValueError("Cinema name required")
        
        if new_cinema.city == None:
            raise ValueError("Cinema city required")

        created_cinema = self.cinemaRepo.createCinema(new_cinema)
        return created_cinema

    def fetchCinema(self, cinemaId):

        if cinemaId == None:
            raise ValueError("Cinema id required")

        fetched_cinema = self.cinemaRepo.fetchCinema(cinemaId)

        return fetched_cinema

    def deleteCinema(self, cinema_to_delete):

        if cinema_to_delete.id == None:
            raise ValueError("Cinema id required")
        
        if cinema_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_cinema = self.cinemaRepo.deleteCinema(cinema_to_delete)

        return deleted_cinema

    def updateCinema(self, cinema_to_update):

        if cinema_to_update.id == None:
            raise ValueError("Cinema id required")

        if cinema_to_update.user_id == None:
            raise ValueError("User id required")

        updated_cinema = self.cinemaRepo.updateCinema(cinema_to_update)

        return updated_cinema

    def createCity(self, new_city):

        if new_city.id == None:
            raise ValueError("City id required")
        
        if new_city.added_by == None:
            raise ValueError("User id required")
        
        if new_city.name == None:
            raise ValueError("Cinema name required")

        created_city = self.cinemaRepo.createCity(new_city)
        return created_city

    def fetchCity(self, cityId):

        if cityId == None:
            raise ValueError("City id required")

        fetched_city = self.cinemaRepo.fetchCity(cityId)

        return fetched_city

    #if we delete what will happen to existing records ???
    #try except here

    def deleteCity(self, city_to_delete):

        if city_to_delete.id == None:
            raise ValueError("City id required")
        
        if city_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_city = self.cinemaRepo.deleteCity(city_to_delete)

        return deleted_city

    def updateCity(self, city_to_update):

        if city_to_update.id == None:
            raise ValueError("City id required")

        if city_to_update.user_id == None:
            raise ValueError("User id required")

        updated_city = self.cinemaRepo.updateCity(city_to_update)

        return updated_city