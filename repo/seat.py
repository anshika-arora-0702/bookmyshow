from sqlalchemy import select

from models.domain.seats.seat import Seat as SeatDomain
from models.database.seats.seat import Seat as SeatDB
from models.database.users.user import User as UserDB
from models.database.users.user_role import UserRole
from models.database.audis.audi import Audi as AudiDB

from exceptions import user_exceptions
from exceptions import seat_exceptions

from datetime import datetime,timezone

from sqlalchemy.exc import IntegrityError
class SeatRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _seat_to_db(self, seat:SeatDomain) -> SeatDB:
        return SeatDB( id = seat.id,
                      audi_id = seat.audi_id,
                      column_num = seat.column_num,
                      row_char = seat.row_char,
                      type = seat.type,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )
    
    def _seat_to_domain(self, seat:SeatDB) -> SeatDomain:
        return SeatDomain( id = seat.id,
                      audi_id = seat.audi_id,
                      column_num = seat.column_num,
                      row_char = seat.row_char,
                      type = seat.type
                      )

    def _seat_type(self, seat_id):

        seat:SeatDB = self.db_session.get(SeatDB, seat_id)

        if seat is None:
            raise seat_exceptions.SeatNotFoundException(seat_id)
        return seat.type

    def _fetch_seat_types(self, seat_ids):

        if not seat_ids:
            raise ValueError("At least one seat ID is required")
        requested_ids = set(seat_ids)

        rows = self.db_session.execute(
            select(SeatDB.id, SeatDB.type).where(
                SeatDB.id.in_(requested_ids)
            )
        ).all()

        seat_types_by_id = {
            seat_id: seat_type
            for seat_id, seat_type in rows
        }

        missing_ids = requested_ids - seat_types_by_id.keys()

        if missing_ids:
            missing_id = next(
                seat_id for seat_id in seat_ids
                if seat_id in missing_ids
            )
            raise seat_exceptions.SeatNotFoundException(missing_id)

        return seat_types_by_id

    def createSeat(self, seat_to_create_domain:SeatDomain):
        
        
        try:
            seat_to_create_db = self._seat_to_db(seat_to_create_domain)
            self.db_session.add(seat_to_create_db )
            self.db_session.flush()
            return self._seat_to_domain(seat_to_create_db )

        except IntegrityError as e:
            raise seat_exceptions.SeatIntegrityException() from e

        except Exception as e:
            raise seat_exceptions.SeatException() from e

    def fetchAudiSeats(self,audi_id):
        seat_ids = self.db_session.scalars(select(SeatDB.id).where(SeatDB.audi_id == audi_id)).all()
        if not seat_ids:
            raise ValueError(f"No seats found for auditorium {audi_id}")
        return seat_ids

    def fetchAudiSeatTypes(self, audi_id):
        seat_types = self.db_session.scalars(select(SeatDB.type).where(SeatDB.audi_id == audi_id).distinct()).all()
        return seat_types