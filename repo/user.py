from models.domain.users.user import User as UserDomain

from models.database.users.user import User as UserDB
from models.database.users.user_role import UserRole

from models.requests.users.fetch_user import FetchUserRequest
from models.requests.users.delete_user import DeleteUserRequest

from exceptions import user_exceptions
from sqlalchemy.exc import IntegrityError

from datetime import datetime,timezone

class UserRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _user_to_db(self,user:UserDomain) -> UserDB:

        return UserDB(id = user.id,
                      dob = user.dob,
                      email = user.email,
                      phone = user.phone,
                      first_name = user.first_name,
                      last_name = user.last_name,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc),
                      role = user.role,
                      hashed_password = user.password
                      )

    def _user_to_domain(self,user:UserDB) -> UserDomain:

        return UserDomain(id = user.id, 
                      dob = user.dob,
                      email = user.email,
                      phone = user.phone,
                      first_name = user.first_name,
                      last_name = user.last_name,
                      role = user.role,
                      password= user.hashed_password
                      )

    def createUser(self, user_to_create_domain:UserDomain):

        if self.db_session.get(UserDB,user_to_create_domain.id) != None:
            raise user_exceptions.UserAlreadyExistsException(user_to_create_domain.id)

        try:
            user_to_create_db = self._user_to_db(user_to_create_domain)
            self.db_session.add(user_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(user_to_create_db)
            return self._user_to_domain(user_to_create_db)

        except Exception :
            self.db_session.rollback()
            raise user_exceptions.UserException()

    def fetchUser(self, user_to_fetch: FetchUserRequest):
                
        fetched_user_db = self.db_session.get(UserDB, user_to_fetch.id)

        if fetched_user_db == None:
            raise user_exceptions.UserDoesnotExistException(user_to_fetch.id)

        fetched_by_user_db = self.db_session.get(UserDB,user_to_fetch.fetched_by)

        if user_to_fetch.id != user_to_fetch.fetched_by:

            if fetched_user_db.role == UserRole.USER:

                if not fetched_by_user_db.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN):
                    raise user_exceptions.UnauthorizedException("User", "fetch")

            elif fetched_user_db.role == UserRole.ADMIN:

                if not fetched_by_user_db.role == UserRole.SUPER_ADMIN: 
                    raise user_exceptions.UnauthorizedException("User", "fetch")

            else :
                raise user_exceptions.UnauthorizedException("User", "fetch")

        return self._user_to_domain(fetched_user_db)

    def deleteUser(self, user_to_delete: DeleteUserRequest):
                
        user_to_delete_db = self.db_session.get(UserDB, user_to_delete.id)
        if user_to_delete_db == None:
            raise user_exceptions.UserDoesnotExistException(user_to_delete.id)

        deleted_by_db = self.db_session.get(UserDB,user_to_delete.deleted_by)
        if deleted_by_db == None:
            raise user_exceptions.UserDoesnotExistException(user_to_delete.deleted_by)

        if user_to_delete.id != user_to_delete.deleted_by:

            if user_to_delete_db.role == UserRole.USER:
                if not deleted_by_db.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN):
                    raise user_exceptions.UnauthorizedException("User", "delete")

            elif user_to_delete_db.role == UserRole.ADMIN:
                if not deleted_by_db.role == UserRole.SUPER_ADMIN: 
                    raise user_exceptions.UnauthorizedException("User", "delete")

            else :
                raise user_exceptions.UnauthorizedException("User", "delete")

        try:
            self.db_session.delete(user_to_delete_db)
            self.db_session.commit()
            return self._user_to_domain(user_to_delete_db)

        except Exception :
            self.db_session.rollback()
            raise user_exceptions()

    def updateUser(self, user_id, updated_by, changes):

        user_to_update_db = self.db_session.get(UserDB, user_id)
        if user_to_update_db == None:
            raise user_exceptions.UserDoesnotExistException(user_id)

        updated_by_db = self.db_session.get(UserDB, updated_by)
        if updated_by_db == None:
            raise user_exceptions.UserDoesnotExistException(updated_by)

        if user_id != updated_by:

            if user_to_update_db.role == UserRole.USER:
                if not updated_by_db.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN):
                    raise user_exceptions.UnauthorizedException("User", "update")

            elif user_to_update_db.role == UserRole.ADMIN:
                if not updated_by_db.role == UserRole.SUPER_ADMIN: 
                    raise user_exceptions.UnauthorizedException("User", "update")

            else :
                raise user_exceptions.UnauthorizedException("User", "update")

        allowed_fields = {"first_name", "last_name", "phone", "email", "dob"}

        for field, value in changes.items():
            if field not in allowed_fields:
                raise user_exceptions.FieldChangeNotAllowed(field)
            setattr(user_to_update_db, field, value)

        user_to_update_db.updated_at = datetime.now(timezone.utc)

        try:
            self.db_session.commit()
            self.db_session.refresh(user_to_update_db)
            return self._user_to_domain(user_to_update_db)

        except IntegrityError as e:
            self.db_session.rollback()
            raise user_exceptions.UserContactAlreadyExistsException() from e

        except Exception as e :
            self.db_session.rollback()
            raise user_exceptions.UserException() from e
        
    def updateRole(self, user_id, updated_by, new_role):

        user_to_update_db = self.db_session.get(UserDB, user_id)
        if user_to_update_db == None:
            raise user_exceptions.UserDoesnotExistException(user_id)

        updated_by_db = self.db_session.get(UserDB, updated_by)
        if updated_by_db == None:
            raise user_exceptions.UserDoesnotExistException(updated_by)


        if user_to_update_db.role == UserRole.USER:
            if not updated_by_db.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN):
                raise user_exceptions.UnauthorizedException("User", "update")

        elif user_to_update_db.role == UserRole.ADMIN:
            if not updated_by_db.role == UserRole.SUPER_ADMIN: 
                raise user_exceptions.UnauthorizedException("Admin", "update")

        else :
            raise user_exceptions.UnauthorizedException("Super Admin", "update")
        
        user_to_update_db.role = new_role
        user_to_update_db.updated_at = datetime.now(timezone.utc)

        try:
            self.db_session.commit()
            self.db_session.refresh(user_to_update_db)
            return self._user_to_domain(user_to_update_db)

        except Exception as e :
            self.db_session.rollback()
            raise user_exceptions.UserException() from e

    
        

        


