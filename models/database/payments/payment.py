from sqlalchemy import Column, Float, REAL, Integer,  UUID, DateTime, ForeignKey
from models.database.base import Base

class Payment(Base):

    __tablename__ = "payment"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    amount = Column(
        REAL,
        nullable=False
    )

    status = Column(
        Integer,
        ForeignKey("payment_status.id"),
        nullable=False
    )

    mode = Column(
        Integer,
        ForeignKey("payment_mode.id"),
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