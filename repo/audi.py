from models.domain.audis.audi import Audi as AudiDomain
from models.database.audis.audi import Audi as AudiDB

from models.database.users.user import User as UserDB
from models.database.cinemas.cinema import Cinema as CinemaDB
from models.database.users.user_role import UserRole

from exceptions import audi_exceptions 
from exceptions import user_exceptions 

from datetime import datetime,timezone

class AudiRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _fetch_audi(self, audi_id):

        if audi_id is None:
            raise ValueError("No audi ifd provided")
        
        audi = self.db_session.get(AudiDB,audi_id)
        if audi is None:
            raise audi_exceptions.AudiNotFoundException(audi_id)
        
        return self._audi_to_domain(audi)

    def _audi_to_db(self,audi:AudiDomain) -> AudiDB:

        return AudiDB(id = audi.id, 
                      cinema_id = audi.cinema_id, 
                      row_count = audi.row_count,  
                      column_count = audi.column_count, 
                      added_by = audi.user_id,
                      type = audi.type,
                      screen_num = audi.screen_num,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )

    def _audi_to_domain(self,audi:AudiDB) -> AudiDomain:

        return AudiDomain(id = audi.id, 
                      cinema_id = audi.cinema_id, 
                      row_count = audi.row_count,  
                      column_count = audi.column_count, 
                      user_id= audi.added_by,
                      type = audi.type,
                      screen_num = audi.screen_num
                      )

    def createAudi(self, audi_to_create_domain:AudiDomain) -> AudiDomain:

        if self.db_session.get(AudiDB,audi_to_create_domain.id) != None:
            raise audi_exceptions.AudiAlreadyExists(audi_to_create_domain.id)

        try:
            audi_to_create_db = self._audi_to_db(audi_to_create_domain)
            self.db_session.add(audi_to_create_db)
            self.db_session.flush()
            return self._audi_to_domain(audi_to_create_db)

        except Exception :
            raise audi_exceptions.AudiException()

    # def fetchAudi(self, audi_to_fetch) -> AudiDomain:

    #     fetched_audi_db = self.db_session.get(AudiDB, audi_to_fetch.id)

    #     if fetched_audi_db == None:
    #         raise e.AudiNotFoundException(audi_to_fetch.id)

    #     return self._audi_to_domain(fetched_audi_db)
    
    # def deleteAudi(self, audi_to_delete):
        
    #     audi_to_delete_db = self.db_session.get(AudiDB, audi_to_delete.id)

    #     if audi_to_delete_db == None:
    #         raise e.AudiNotFoundException(audi_to_delete.id)

    #     user = self.db_session.get(UserDB,audi_to_delete.user_id)

    #     if not (
    #         (user.role == 'SUPER_ADMIN') or 
    #         ((audi_to_delete_db.added_by == audi_to_delete.user_id) and (user.role == 'ADMIN'))
    #         ):
    #         raise user_exceptions.UnauthorizedException("Audi", "delete")

    #     try:
    #         self.db_session.delete(audi_to_delete_db)
    #         self.db_session.commit()
    #         return self._audi_to_domain(audi_to_delete_db)

    #     except Exception :
    #         self.db_session.rollback()
    #         raise e.AudiException()

    # def updateAudi(self, audi_to_update):

    #     audi_to_update_db = self.db_session.get(AudiDB, audi_to_update.id)

    #     if audi_to_update_db == None:
    #         raise e.AudiNotFoundException(audi_to_update.id)

    #     user = self.db_session.get(UserDB,audi_to_update.user_id)

    #     if not (
    #         (user.role == 'SUPER_ADMIN') or 
    #         ((audi_to_update_db.added_by == user.id) and (user.role == 'ADMIN'))
    #         ):
    #         raise user_exceptions.UnauthorizedException("Audi", "update")
        

    #     try:
    #         audi_to_update_db.cinema_id = audi_to_update.cinema_id
    #         audi_to_update_db.row_count = audi_to_update.row_count
    #         audi_to_update_db.column_count = audi_to_update.column_count
    #         audi_to_update_db.type = audi_to_update.type
    #         audi_to_update_db.screen_num = audi_to_update.screen_num
    #         audi_to_update_db.updated_at = datetime.now(timezone.utc)
            
    #         self.db_session.commit()
    #         self.db_session.refresh(audi_to_update_db)
    #         return self._audi_to_domain(audi_to_update_db)

    #     except Exception :
    #         self.db_session.rollback()
    #         raise e.AudiException()
