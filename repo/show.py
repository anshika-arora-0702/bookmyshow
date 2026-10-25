from models.domain.shows.show import Show as ShowDomain
from models.database.shows.show import Show as ShowDB
from models.database.shows.show_seat_availability import ShowSeatAvailability
from exceptions import booking_exceptions

from exceptions import show_exceptions

from datetime import datetime,timezone

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update
class ShowRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _calculate_show_seats_price(self,show_id, seat_ids):

        if not show_id:
            raise ValueError("No show provided")
        
        show:ShowDB = self.db_session.get(ShowDB, show_id)

        if show is None:
            raise show_exceptions.ShowNotFoundException(show_id)

        if not seat_ids:
            raise ValueError("At least one seat is required")

        requested_ids = set(seat_ids)

        if len(requested_ids) != len(seat_ids):
            raise ValueError("Duplicate seat ids provided")
        
        
        rows = self.db_session.execute(
            select(
                ShowSeatAvailability.seat_id,
                ShowSeatAvailability.availability,
            ).where(
                ShowSeatAvailability.show_id == show_id,
                ShowSeatAvailability.seat_id.in_(requested_ids),
            )
        ).all()

        rows_by_id = {row.seat_id: row.availability for row in rows}
        missing_ids = requested_ids - rows_by_id.keys()

        if missing_ids:
            raise ValueError(f"These seats do not belong to this show: {missing_ids}")
        
        unavailable_ids = {seat_id for seat_id, available in rows_by_id.items() if not available}

        if unavailable_ids:
            raise ValueError(f"These seats are unavailable: {unavailable_ids}")

        return show.price_dict

    def reserveSeats(self,show_id,seat_ids,booking_id):

        result = self.db_session.execute(update(ShowSeatAvailability).where(
                ShowSeatAvailability.show_id == show_id,
                ShowSeatAvailability.seat_id.in_(seat_ids),
                ShowSeatAvailability.availability.is_(True),
            )
            .values(
                availability=False,
                booking_id=booking_id,
                updated_at=datetime.now(timezone.utc),
            )
        )

        if result.rowcount !=  len(seat_ids):
            raise show_exceptions.ShowSeatException(show_id,"one or more requested seats are unavailable")


        self.db_session.flush()

    def releaseSeats(self, booking_id, show_id, seat_ids):

        try: 
            for seat_id in seat_ids:
                    show_seat : ShowSeatAvailability = self.db_session.get(ShowSeatAvailability, (show_id, seat_id))
                    if show_seat.booking_id == booking_id:
                        show_seat.availability = True
                        show_seat.booking_id = None
                        show_seat.updated_at = datetime.now(timezone.utc)

        except Exception as error:
            raise 



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
                          price= show.price_dict
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
