from pydantic import UUID4
from models.domain.payments.payment import Payment
from models.database.payments.payment_status import PaymentStatus
class PaymentService():

    def __init__(self, paymentRepo, paymentProvider):
        self.paymentRepo = paymentRepo
        self.paymentProvider = paymentProvider

    def _validate_payment(payment):

        if payment.amount == None:
            raise ValueError("Error in fetching payment amount from booking")
        
        if payment.mode == None:
            raise ValueError("Error in fetching payment mode from booking")

    def createPendingPayment(self, new_payment: Payment):
        created_payment = self.paymentRepo.createPendingPayment(new_payment)
        return created_payment

    def processPayment(self, payment, user_id):
        return self.paymentProvider.charge(payment, user_id)

    def cancelPayment(self,payment, user_id):
        return self.paymentProvider.cancel(payment,user_id)

    def markSuccessful(self, payment_id):
        self.paymentRepo.markSuccessful(payment_id)
        return

    def markFailed(self, payment_id):
        self.paymentRepo.markFailed(payment_id)
        return
    
    def markCancelled(self, payment_id):
        self.paymentRepo.markCancelled(payment_id)
        return

    def fetchPayment(self, paymentId):

        if paymentId == None:
            raise ValueError("Payment id required")

        fetched_payment = self.paymentRepo.fetchPayment(paymentId)

        return fetched_payment
