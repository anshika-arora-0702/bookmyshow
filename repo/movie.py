from models.domain.movies.movie import Movie as MovieDomain

from models.database.movies.movie import Movie as MovieDB
from models.database.users.user import User as UserDB

from models.requests.movies.create_movie import CreateMovieRequest

from exceptions import user_exceptions
from exceptions import movie_exceptions
from sqlalchemy.exc import IntegrityError

from datetime import datetime,timezone

class MovieRepo:

    def __init__(self, db_session):
        self.db_session = db_session


    def _fetch_movie(self,movie_id) -> MovieDomain:
        movie = self.db_session.get(MovieDB, movie_id)
        if movie is None:
            raise movie_exceptions.MovieNotFoundException(movie_id)
        return self._movie_to_domain(movie)

    def _movie_to_db(self,movie:MovieDomain) -> MovieDB:

        return MovieDB(id= movie.id,
                       name = movie.name,
                       added_by = movie.added_by,
                       poster = movie.poster,
                       runtime_in_sec = movie.runtime_in_sec,
                       release_date = movie.release_date,
                       details = movie.details,
                       created_at = datetime.now(timezone.utc),
                       updated_at = datetime.now(timezone.utc)
                       )

    def _movie_to_domain(self,movie:MovieDB) -> MovieDomain:

        return MovieDomain(id = movie.id,
                          name= movie.name,
                          added_by= movie.added_by,
                          poster= movie.poster,
                          runtime_in_sec=movie.runtime_in_sec,
                          release_date= movie.release_date,
                          details=movie.details
                          )

    def createMovie(self, movie_to_create_domain:MovieDomain):

        user = self.db_session.get(UserDB,movie_to_create_domain.added_by)

        if user == None:
            raise user_exceptions.UserDoesnotExistException()

        if user.role not in ('SUPER_ADMIN', 'ADMIN'):
            raise user_exceptions.UnauthorizedException("Movie", "create")
        
        try:
            movie_to_create_db = self._movie_to_db(movie_to_create_domain)
            self.db_session.add(movie_to_create_db)
            self.db_session.commit()
            self.db_session.refresh(movie_to_create_db)
            return self._movie_to_domain(movie_to_create_db)

        except IntegrityError as e:
            self.db_session.rollback()
            raise movie_exceptions.MovieIntegrityException() from e

        except Exception :
            self.db_session.rollback()
            raise movie_exceptions.CityException()