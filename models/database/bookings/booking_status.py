from enum import Enum

class BookingStatus(str, Enum):
    CANCELLED = "CANCELLED"
    BOOKED = "BOOKED"
    PENDING = "PENDING"
    FAILED = "FAILED"
