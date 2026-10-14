from pydantic import UUID4

class PaymentException(Exception):
    pass

class PaymentNotFoundException(PaymentException):

    def __init__(self, payment_id:UUID4):
        self.payment_id = payment_id
        super().__init__(f"Show with id '{payment_id}' not found")

class PaymentPending(PaymentException):

    def __init__(self):
        super().__init__(f"Payment Pending")

class PaymentFailed(PaymentException):

    def __init__(self):
        super().__init__(f"Payment Failed")