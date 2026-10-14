from sqlalchemy import Column, String, Text,Integer, UUID, DateTime, ForeignKey
from models.database.base import Base

class Cinema(Base):

    __tablename__ = "cinema"

    id =  Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        nullable=False
    )

    name = Column(
        String, 
        nullable=False
    )

    added_by = Column(
        UUID,
        ForeignKey("user.id"),
        nullable=False
    )

    address = Column(
        Text,
        nullable=True
    )

    city = Column(
        Integer, 
        ForeignKey("city.id"),
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