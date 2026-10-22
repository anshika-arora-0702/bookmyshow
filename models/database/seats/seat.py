from sqlalchemy import Column, String, Integer, UUID, DateTime, ForeignKey, Enum, UniqueConstraint, PrimaryKeyConstraint
from models.database.seats.seat_type import SeatType
from models.database.base import Base

class Seat(Base):

    __tablename__ = "seat"

    __table_args__ = (
        PrimaryKeyConstraint("audi_id", "id"),
        UniqueConstraint(
            "audi_id",
            "row_char",
            "column_num",
            name="uq_seat_audi_row_column"
        ),
    )

    id = Column(
        UUID(as_uuid = True),
        unique=True,
        nullable=False
    )

    audi_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("audi.id"), 
        nullable=False
    )

    column_num = Column(
        Integer, 
        nullable=False
    )

    row_char = Column(
        String, 
        nullable= False
    )

    type = Column(
        Enum(SeatType, name="seat_type"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )