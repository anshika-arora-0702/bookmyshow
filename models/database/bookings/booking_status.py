from enum import Enum

class BookingStatus(str, Enum):
    CANCELLED = "Cancelled"
    BOOKED = "Booked"
    CONFIRMATION_PENDING = "Confirmation Pending"
