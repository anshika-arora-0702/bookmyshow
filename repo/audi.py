from models.domain.audis.audi import Audi as AudiDomain
from models.database.audis.audi import Audi as AudiDB

from models.database.users.user import User as UserDB

from exceptions import audi_exceptions as e
from exceptions import auth_exceptions as ae

from datetime import datetime,timezone

class AudiRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _audi_to_db(self,audi:AudiDomain) -> AudiDB:

        return AudiDB(id = audi.id, 
                      cinema_id = audi.cinema_id, 
                      row_count = audi.row_count,  
                      column_count = audi.column_count, 
                      added_by = audi.added_by,
                      type = audi.type,
                      screen_num = audi.screen_num,
                      created_at = datetime.utcnow(),
                      updated_at = datetime.utcnow()
                      )

    def _audi_to_domain(self,audi:AudiDB) -> AudiDomain:

        return AudiDomain(id = audi.id, 
                      cinema_id = audi.cinema_id, 
                      row_count = audi.row_count,  
                      column_count = audi.column_count, 
                      added_by = audi.added_by,
                      type = audi.type,
                      screen_num = audi.screen_num
                      )

    def createAudi(self, audi_to_create_domain:AudiDomain) -> AudiDomain:

        audi_to_create_db = self._audi_to_db(audi_to_create_domain)

        if self.db_session.get(AudiDB,audi_to_create_db.id) != None:
            raise e.AudiAlreadyExists(audi_to_create_db.id)

        user = self.db_session.get(UserDB,audi_to_create_db.added_by)

        if user == None:
            raise ae.UserDoesnotExistException()

        if user.role not in ('SUPER_ADMIN', 'ADMIN'):
            raise ae.UnauthorizedException("Audi", "create")

        try:
            self.db_session.add(audi_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(audi_to_create_db)
            return self._audi_to_domain(audi_to_create_db)

        except Exception :
            self.db_session.rollback()
            raise e.AudiException()

    def fetchAudi(self, audi_to_fetch) -> AudiDomain:

        fetched_audi_db = self.db_session.get(AudiDB, audi_to_fetch.id)

        if fetched_audi_db == None:
            raise e.AudiNotFoundException(audi_to_fetch.id)

        return self._audi_to_domain(fetched_audi_db)
    
    def deleteAudi(self, audi_to_delete):
        
        audi_to_delete_db = self.db_session.get(AudiDB, audi_to_delete.id)

        if audi_to_delete_db == None:
            raise e.AudiNotFoundException(audi_to_delete.id)

        user = self.db_session.get(UserDB,audi_to_delete.user_id)

        if not (
            (user.role == 'SUPER_ADMIN') or 
            ((audi_to_delete_db.added_by == audi_to_delete.user_id) and (user.role == 'ADMIN'))
            ):
            raise ae.UnauthorizedException("Audi", "delete")

        try:
            self.db_session.delete(audi_to_delete_db)
            self.db_session.commit()
            return self._audi_to_domain(audi_to_delete_db)

        except Exception :
            self.db_session.rollback()
            raise e.AudiException()

    def updateAudi(self, audi_to_update):

        audi_to_update_db = self.db_session.get(AudiDB, audi_to_update.id)

        if audi_to_update_db == None:
            raise e.AudiNotFoundException(audi_to_update.id)

        user = self.db_session.get(UserDB,audi_to_update.user_id)

        if not (
            (user.role == 'SUPER_ADMIN') or 
            ((audi_to_update_db.added_by == user.id) and (user.role == 'ADMIN'))
            ):
            raise ae.UnauthorizedException("Audi", "update")
        

        try:
            audi_to_update_db.cinema_id = audi_to_update.cinema_id
            audi_to_update_db.row_count = audi_to_update.row_count
            audi_to_update_db.column_count = audi_to_update.column_count
            audi_to_update_db.type = audi_to_update.type
            audi_to_update_db.screen_num = audi_to_update.screen_num
            audi_to_update_db.updated_at = datetime.now(timezone.utc)
            
            self.db_session.commit()
            self.db_session.refresh(audi_to_update_db)
            return self._audi_to_domain(audi_to_update_db)

        except Exception :
            self.db_session.rollback()
            raise e.AudiException()
