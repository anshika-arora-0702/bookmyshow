from sqlalchemy import Column, Integer, String, Date, UUID, DateTime
from models.database.base import Base

class User(Base):

    __tablename__ = "user"

    id =  Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        nullable=False
    )

    first_name = Column(
        String, 
        nullable=False 
    )

    role = Column(
        String, 
        nullable=False 
    )

    last_name = Column(
        String, 
        nullable=True
    )

    phone = Column(
        Integer, 
        nullable=False, 
        unique=True
    )

    email = Column(
        String, 
        nullable=True, 
        unique=True
    )

    dob = Column(
        Date, 
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