class AudiService():

    def __init__(self, audiRepo):
        self.audiRepo = audiRepo

    def createAudi(self, new_audi):

        if new_audi.id == None:
            raise ValueError("Error in creating audi id")
        
        if new_audi.added_by == None:
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

        created_audi = self.audiRepo.createAudi(new_audi)
        return created_audi

    def fetchAudi(self, audi_to_fetch):

        if audi_to_fetch.id == None:
            raise ValueError("Audi id required")

        if audi_to_fetch.user_id == None:
            raise ValueError("User id required")

        fetched_audi = self.audiRepo.fetchAudi(audi_to_fetch)

        return fetched_audi

    def deleteAudi(self, audi_to_delete):

        if audi_to_delete.id == None:
            raise ValueError("Audi id required")
        
        if audi_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_audi = self.audiRepo.deleteAudi(audi_to_delete)

        return deleted_audi

    def updateAudi(self, audi_to_update):

        if audi_to_update.id == None:
            raise ValueError("Audi id required")

        if audi_to_update.user_id == None:
            raise ValueError("User id required")

        updated_audi = self.audiRepo.updateAudi(audi_to_update)

        return updated_audi

    def createAudiType(self, new_audi_type):

        if new_audi_type.id == None:
            raise ValueError("Audi Type id required")
        
        if new_audi_type.added_by == None:
            raise ValueError("User id required")
        
        if new_audi_type.name == None:
            raise ValueError("Audi Type name required")

        created_audi_type = self.audiRepo.createAudiType(new_audi_type)
        return created_audi_type

    def fetchAudiType(self, audi_typeId):

        if audi_typeId == None:
            raise ValueError("Audi Type id required")

        #do we need to verify user here???

        fetched_audi_type = self.audiRepo.fetchAudiType(audi_typeId)

        return fetched_audi_type

    def deleteAudiType(self, audi_type_to_delete):

        if audi_type_to_delete.id == None:
            raise ValueError("Audi Type id required")
        
        if audi_type_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_audi_type = self.audiRepo.deleteAudiType(audi_type_to_delete)

        return deleted_audi_type

    def updateAudiType(self, audi_type_to_update):

        if audi_type_to_update.id == None:
            raise ValueError("Audi Type id required")

        if audi_type_to_update.user_id == None:
            raise ValueError("User id required")

        updated_audi_type = self.audiRepo.updateAudiType(audi_type_to_update)

        return updated_audi_type