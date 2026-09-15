from sqlalchemy import Column, Boolean, UUID, DateTime, ForeignKey
from models.database.base import Base

class ShowSeatAvailability(Base):

    __tablename__ = "show_seat_availability"

    show_id =  Column(
        UUID(as_uuid=True), 
        ForeignKey("show.id"),
        primary_key=True, 
        nullable=False
    )

    seat_id = Column(
        UUID(as_uuid=True),
        ForeignKey("seat.id"), 
        primary_key=True,
        nullable=False
    )

    booking_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("booking.id"), 
        nullable=True
    )

    availability = Column(
        Boolean, 
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