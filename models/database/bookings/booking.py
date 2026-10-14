from sqlalchemy import Column, Integer, JSON, UUID, DateTime, ForeignKey, Enum, ARRAY
from models.database.base import Base
from models.database.bookings.booking_status import BookingStatus

class Booking(Base):

    __tablename__ = "booking"

    id =  Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        nullable=False
    )

    user_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("user.id"),
        nullable=False
    )
    
    show_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("show.id"),
        nullable=False
    )

    payment_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("payment.id"),
        nullable=False
    )

    status = Column(
        Enum(BookingStatus, name="booking_status"),
        nullable=False
    )

    seat_ids = Column(
        ARRAY(UUID),
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

    requested_time = Column(
        DateTime(timezone=True),
        nullable = False
    )

    booking_time = Column(
        DateTime(timezone=True),
        nullable=True
    )
