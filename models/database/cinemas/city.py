from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models.database.base import Base

class City(Base):

    __tablename__ = "city"

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
        String,
        ForeignKey("user.id"),
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