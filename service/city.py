from models.domain.city.city import City

class CityService():

    def __init__(self, cityRepo):
        self.cityRepo = cityRepo


    def createCity(self, new_city:City):
        
        if new_city.added_by == None:
            raise ValueError("User id required")
        
        if new_city.name == None:
            raise ValueError("City name required")

        created_city = self.cityRepo.createCity(new_city)
        return created_city

    def fetchCity(self, cityId):

        if cityId == None:
            raise ValueError("City id required")

        fetched_city = self.cityRepo.fetchCity(cityId)

        return fetched_city

    #if we delete what will happen to existing records ???
    #try except here

    def deleteCity(self, city_to_delete):

        if city_to_delete.id == None:
            raise ValueError("City id required")
        
        if city_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_city = self.cityRepo.deleteCity(city_to_delete)

        return deleted_city

    def updateCity(self, city_to_update):

        if city_to_update.id == None:
            raise ValueError("City id required")

        if city_to_update.user_id == None:
            raise ValueError("User id required")

        updated_city = self.cityRepo.updateCity(city_to_update)

        return updated_city