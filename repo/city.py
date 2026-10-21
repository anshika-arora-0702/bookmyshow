from models.domain.city.city import City as CityDomain

from models.database.city.city import City as CityDB
from models.database.users.user import User as UserDB

from models.requests.city.update_city import UpdateCityRequest

from exceptions import user_exceptions
from exceptions import city_exceptions
from sqlalchemy.exc import IntegrityError

from datetime import datetime,timezone

class CityRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _city_to_db(self,city:CityDomain) -> CityDB:

        return CityDB(id = None,
                      name = city.name,
                      added_by = city.added_by,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )

    def _city_to_domain(self,city:CityDB) -> CityDomain:

        return CityDomain(id = city.id,
                          name= city.name,
                          added_by= city.added_by
                          )

    def createCity(self, city_to_create_domain:CityDomain):

        user = self.db_session.get(UserDB,city_to_create_domain.added_by)

        if user == None:
            raise user_exceptions.UserDoesnotExistException()

        if user.role not in ('SUPER_ADMIN', 'ADMIN'):
            raise user_exceptions.UnauthorizedException("City", "create")
        
        try:
            city_to_create_db = self._city_to_db(city_to_create_domain)
            self.db_session.add(city_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(city_to_create_db)
            return self._city_to_domain(city_to_create_db)

        except IntegrityError:
            self.db_session.rollback()
            raise city_exceptions.CityAlreadyExistsException()

        except Exception :
            self.db_session.rollback()
            raise city_exceptions.CityException()