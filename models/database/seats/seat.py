from sqlalchemy import Column, String, Integer, UUID, DateTime, ForeignKey, UniqueConstraint
from models.database.base import Base

class Seat(Base):

    __tablename__ = "seat"

    __table_args__ = (
        UniqueConstraint(
            "audi_id",
            "row_char",
            "column_num",
            name="uq_seat_audi_row_column"
        ),
    )

    id = Column(
        Integer,
        unique=True,
        nullable=False
    )

    audi_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("audi.id"), 
        nullable=False
    )

    column_num = Column(
        Integer, 
        nullable=False
    )

    row_char = Column(
        String, 
        nullable= False
    )

    type = Column(
        Integer, 
        ForeignKey("seat_type.id"),
        nullable = False
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