from models.domain.cinemas.cinema import Cinema as CinemaDomain

from models.database.cinemas.cinema import Cinema as CinemaDB
from models.database.users.user import User as UserDB

from exceptions import user_exceptions
from exceptions import cinema_exceptions
from sqlalchemy.exc import IntegrityError

from datetime import datetime,timezone

class CinemaRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _cinema_to_db(self, cinema:CinemaDomain) -> CinemaDB:

        return CinemaDB(id = cinema.id,
                        name = cinema.name,
                        added_by = cinema.added_by,
                        address = cinema.address,
                        city = cinema.city,
                        created_at = datetime.now(timezone.utc),
                        updated_at = datetime.now(timezone.utc)
                        )

    def _cinema_to_domain(self, cinema:CinemaDB) -> CinemaDomain:
        return CinemaDomain(id = cinema.id,
                            added_by= cinema.added_by,
                            name = cinema.name,
                            address=cinema.address,
                            city=cinema.city) 

    def createCinema(self, cinema_to_create_domain: CinemaDomain):
        user = self.db_session.get(UserDB,cinema_to_create_domain.added_by)

        if user == None:
            raise user_exceptions.UserDoesnotExistException()

        if user.role not in ('SUPER_ADMIN', 'ADMIN'):
            raise user_exceptions.UnauthorizedException("City", "create")
        
        try:
            cinema_to_create_db = self._cinema_to_db(cinema_to_create_domain)
            self.db_session.add(cinema_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(cinema_to_create_db)
            return self._cinema_to_domain(cinema_to_create_db)

        except IntegrityError as e:
            self.db_session.rollback()
            raise cinema_exceptions.CinemaIntegrityException() from e

        except Exception :
            self.db_session.rollback()
            raise cinema_exceptions.CinemaException()
