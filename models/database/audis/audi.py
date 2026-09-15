from sqlalchemy import Column, String, Integer, UUID, DateTime, ForeignKey, Enum
from models.database.base import Base
from models.database.audis.audi_type import AudiType


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
        Enum(AudiType, name="audi_type"),
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