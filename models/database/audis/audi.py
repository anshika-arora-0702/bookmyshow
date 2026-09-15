from sqlalchemy import Column, String, Integer, UUID, DateTime, ForeignKey
from models.database.base import Base


class Audi(Base):

    __tablename__ = "audi"

    id =  Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        nullable=False
    )

    added_by = Column(
        String,
        ForeignKey("user.id"),
        nullable=False
    )    

    cinema_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("cinema.id"),
        nullable=False
    )

    screen_num = Column(
        Integer,
        nullable=False
    )

    row_count = Column(
        Integer, 
        nullable=False
    )

    column_count = Column(
        Integer, 
        nullable= False
    )

    type = Column(
        Integer, 
        ForeignKey("audi_type.id"),
        nullable = False
    )
    
    created_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )