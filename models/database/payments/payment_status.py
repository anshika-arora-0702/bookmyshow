from sqlalchemy import Column, Integer, String, DateTime
from models.database.base import Base

class PaymentStatus(Base):

    __tablename__ = "payment_status"

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

    created_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False
    )