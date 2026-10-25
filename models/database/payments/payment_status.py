from enum import Enum

class PaymentStatus(str, Enum):
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"