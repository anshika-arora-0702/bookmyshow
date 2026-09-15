from sqlalchemy import Column, Integer,  String, DateTime, ForeignKey
from models.database.base import Base

class BookingStatus(Base):

    __tablename__ = "booking_status"

    id =  Column(
        Integer, 
        primary_key=True,
        nullable=False
    )

    added_by = Column(
        String,
        ForeignKey("user.id"),
        nullable=False
    )

    name = Column(
        String,
        nullable=False,
        unique=True
    )

    created_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )