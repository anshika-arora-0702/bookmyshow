from sqlalchemy import Column, Enum, REAL, UUID, DateTime, Numeric
from models.database.base import Base
from models.database.payments.payment_status import PaymentStatus
from models.database.payments.payment_mode import PaymentMode

class Payment(Base):

    __tablename__ = "payment"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    amount = Column(
        Numeric(12,2),
        nullable=False
    )

    status = Column(
        Enum(PaymentStatus, name = "payment_status"),
        nullable=False
    )

    mode = Column(
        Enum(PaymentMode, name = "payment_mode"),
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