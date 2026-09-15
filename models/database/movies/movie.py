from sqlalchemy import Column, String, Integer, Text,  UUID, DateTime, Date, ForeignKey
from models.database.base import Base

class Movie(Base):

    __tablename__ = "movie"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    name = Column(
        Text,
        nullable=False
    )

    added_by = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        nullable= False,
    )

    poster = Column(
        Text,
        nullable=True
    )

    runtime_in_sec = Column(
        Integer,
        nullable=True
    )

    release_date = Column(
        Date,
        nullable=True
    )

    details = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )