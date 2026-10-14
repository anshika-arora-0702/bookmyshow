from models.domain.users.user import User as UserDomain
from models.database.users.user import User as UserDB
from models.database.users.user_role import UserRole
from models.requests.users.fetch_user import FetchUserRequest
from exceptions import user_exceptions

from pydantic import UUID4
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
                      role = UserRole.USER
                      )

    def _user_to_domain(self,user:UserDB) -> UserDomain:

        return UserDomain(id = user.id, 
                      dob = user.dob,
                      email = user.email,
                      phone = user.phone,
                      first_name = user.first_name,
                      last_name = user.last_name,
                      role = UserRole.USER
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
        
    def createAdmin(self, admin_to_create_domain:UserDomain, created_by: UUID4):

        if self.db_session.get(UserDB,admin_to_create_domain.id) != None:
            raise user_exceptions.UserAlreadyExistsException(admin_to_create_domain.id)

        created_by_role = self.db_session.get(UserDB, created_by).role

        if (created_by_role == UserRole.USER) or (created_by_role == UserRole.ADMIN):
            raise user_exceptions.UnauthorizedException("admin","create") 

        try:
            admin_to_create_db = self._user_to_db(admin_to_create_domain)
            self.db_session.add(admin_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(admin_to_create_db)
            return self._user_to_domain(admin_to_create_db)

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

