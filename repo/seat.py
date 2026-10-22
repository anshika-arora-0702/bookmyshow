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