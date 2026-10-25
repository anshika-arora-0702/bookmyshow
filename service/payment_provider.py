from models.database.payments.payment_status import PaymentStatus

class FakePaymentProvider:

    def __init__(self, result=PaymentStatus.SUCCESSFUL):
        self.result = result

    def charge(self, payment_amount, payment_mode, user_id):
        return self.result

    def cancel(self,payment, user_id):
        return PaymentStatus.CANCELLED

    def get_payment_status(self, payment_id):
        return self.result