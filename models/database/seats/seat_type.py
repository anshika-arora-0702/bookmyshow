from sqlalchemy import Column, Integer,  String, DateTime, ForeignKey, UUID
from models.database.base import Base

class SeatType(Base):

    __tablename__ = "seat_type"

    id =  Column(
        Integer, 
        primary_key=True,
        nullable=False
    )

    name = Column(
        String,
        nullable=False,
        unique=True
    )

    added_by = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        nullable= False,
    )

    created_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )