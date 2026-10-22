from models.domain.shows.show import Show as ShowDomain
from models.database.shows.show import Show as ShowDB
from models.database.shows.show_seat_availability import ShowSeatAvailability

from exceptions import show_exceptions

from datetime import datetime,timezone

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
class ShowRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _validate_time(self,audi_id, proposed_start_time, proposed_end_time):

        conflict_id = self.db_session.scalar(select(ShowDB.id).where(
            ShowDB.audi_id == audi_id,
            ShowDB.start_time < proposed_end_time,
            ShowDB.end_time > proposed_start_time).limit(1)
        )

        if conflict_id is not None:
            raise ValueError("This auditorium already has a show during that time")

    def _show_to_db(self, show:ShowDomain, end_time) -> ShowDB:

        return ShowDB( id = show.id,
                      audi_id = show.audi_id,
                      movie_id = show.movie_id,
                      start_time = show.start_time,
                      price = show.price  ,
                      added_by = show.added_by,
                      end_time = end_time,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )
    
    def _show_to_domain(self, show:ShowDB) -> ShowDomain:
        return ShowDomain( id = show.id,
                          added_by= show.added_by,
                          audi_id = show.audi_id,
                          movie_id = show.movie_id,
                          start_time= show.start_time,
                          price= show.price
                          )

    def createShow(self,show_to_create_domain: ShowDomain, end_time):

        if self.db_session.get(ShowDB,show_to_create_domain.id) != None:
            raise show_exceptions.ShowAlreadyExists(show_to_create_domain.id)

        try:
            show_to_create_db = self._show_to_db(show_to_create_domain, end_time)
            self.db_session.add( show_to_create_db)
            self.db_session.flush()
            return self._show_to_domain( show_to_create_db)

        except IntegrityError as e:
            raise show_exceptions.ShowIntegrityException() from e

        except Exception as e :
            raise show_exceptions.ShowException() from e

    def createShowSeats(self, show_id, seat_list):

        for seat_id in seat_list:
            row = ShowSeatAvailability(
                show_id=show_id,
                seat_id=seat_id,
                availability=True,
                booking_id=None,
                created_at = datetime.now(timezone.utc),
                updated_at = datetime.now(timezone.utc)
            )
            self.db_session.add(row)
        self.db_session.flush()
