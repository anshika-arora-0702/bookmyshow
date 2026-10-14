from enum import Enum

class SeatType(str, Enum):
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"
    RECLINER = "RECLINER"
    EXECUTIVE = "EXECUTIVE"