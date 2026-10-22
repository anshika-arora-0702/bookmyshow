from sqlalchemy import Column, UUID, DateTime, ForeignKey, JSON
from models.database.base import Base

class Show(Base):

    __tablename__ = "show"

    id =  Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        nullable=False
    )

    audi_id = Column(
        UUID(as_uuid=True),
        ForeignKey("audi.id"), 
        nullable=False
    )

    movie_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("movie.id"), 
        nullable=False
    )

    start_time = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    price = Column(
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