from models.database.payments.payment_status import PaymentStatus

class FakePaymentProvider:

    def charge(self,payment,user_id):
        return PaymentStatus.SUCCESSFUL

    def cancel(self,payment, user_id):
        return PaymentStatus.CANCELLED