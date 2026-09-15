from sqlalchemy import Column, Integer, JSON, UUID, DateTime, ForeignKey
from models.database.base import Base

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

    payment_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("payment.id"),
        nullable=False
    )

    # payment_mode = Column(
    #     Integer, 
    #     ForeignKey("payment_mode.id"),
    #     nullable=False
    # )

    status = Column(
        Integer, 
        ForeignKey("booking_status_type.id"),
        nullable = False
    )

    seats = Column(
        JSON,
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