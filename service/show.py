class ShowService():

    def __init__(self, showRepo):
        self.showRepo = showRepo

    #jab show add hoga tab uski seats bhi add hongi show seat availability mein
    def createShow(self, new_show):

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

        created_show = self.ShowRepo.createShow(new_show)
        return created_show

    def fetchShow(self, showId):

        if showId == None:
            raise ValueError("Show id required")

        fetched_show = self.ShowRepo.fetchShow(showId)

        return fetched_show

    def deleteShow(self, show_to_delete):

        if show_to_delete.id == None:
            raise ValueError("Show id required")
        
        if show_to_delete.deleted_by_id == None:
            raise ValueError("Deleted by id required")

        deleted_show = self.ShowRepo.deleteShow(show_to_delete)

        return deleted_show

    def updateShow(self, show_to_update):

        if show_to_update.id == None:
            raise ValueError("Show id required")

        if show_to_update.updates_by_id == None:
            raise ValueError("Updates by id is required")

        updated_show = self.showRepo.updateShow(show_to_update)

        return updated_show

    def fetchShowSeatAvailability(self, showId):

        if showId == None:
            raise ValueError("Show id required")

        fetched_show_seat_availability = self.ShowRepo.fetchShowSeatAvailability(showId)

        return fetched_show_seat_availability

    #when a booking is made or cancelled
    def updateShowSeatAvailability(self, show_seat_availability_to_update):

        if show_seat_availability_to_update.show_id == None:
            raise ValueError("Show id required")
        
        if show_seat_availability_to_update.seats == None:
            raise ValueError("Seats required")
        
        if show_seat_availability_to_update.booking_id == None:
            raise ValueError("Booking id required")

        updated_show_seat_availability = self.ShowRepo.updateShowSeatAvailability(show_seat_availability_to_update)

        return updated_show_seat_availability


