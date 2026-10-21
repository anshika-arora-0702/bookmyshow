from sqlalchemy import Column, Integer, String, Date, UUID, DateTime, Enum
from models.database.base import Base
from models.database.users.user_role import UserRole

class User(Base):

    __tablename__ = "user"

    id =  Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        nullable=False
    )

    hashed_password = Column(
        String(255),
        nullable=True
    )

    first_name = Column(
        String, 
        nullable=False 
    )

    role = Column(
        Enum(UserRole, name = "user_role"), 
        nullable=False 
    )

    last_name = Column(
        String, 
        nullable=True
    )

    phone = Column(
        String, 
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

