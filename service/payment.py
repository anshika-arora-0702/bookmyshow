from pydantic import UUID4
from models.domain.payments.payment import Payment as PaymentDomain
from models.database.payments.payment_status import PaymentStatus
from repo.payment import PaymentRepo
from service.payment_provider import FakePaymentProvider
class PaymentService():

    def __init__(self, paymentRepo : PaymentRepo, paymentProvider: FakePaymentProvider):
        self.paymentRepo = paymentRepo
        self.paymentProvider = paymentProvider

    def _validate_payment(self, payment:PaymentDomain):

        if payment.amount == None:
            raise ValueError("Error in fetching payment amount from booking")
        
        if payment.mode == None:
            raise ValueError("Error in fetching payment mode from booking")
        
        if payment.id == None:
            raise ValueError("Error in creating payment id")
        
        if payment.status == None:
            raise ValueError("Error in setting payment status")

    def createPendingPayment(self, new_payment: PaymentDomain):
        self._validate_payment(new_payment)
        created_payment = self.paymentRepo.createPendingPayment(new_payment)
        return created_payment

    def processPayment(self, payment : PaymentDomain, user_id):
        return self.paymentProvider.charge(payment.amount, payment.mode, user_id)

    # def cancelPayment(self,payment, user_id):
    #     return self.paymentProvider.cancel(payment,user_id)

    def markSuccessful(self, payment_id):
        self.paymentRepo.markSuccessful(payment_id)
        return

    def markFailed(self, payment_id):
        self.paymentRepo.markFailed(payment_id)
        return

    def markUnknown(self, payment_id):
        self.paymentRepo.markUnknown(payment_id)

    def get_payment_status(self, payment_id):
        return self.paymentProvider.get_payment_status(payment_id)
    
    # def markCancelled(self, payment_id):
    #     self.paymentRepo.markCancelled(payment_id)
    #     return

    # def fetchPayment(self, paymentId):

    #     if paymentId == None:
    #         raise ValueError("Payment id required")

    #     fetched_payment = self.paymentRepo.fetchPayment(paymentId)

    #     return fetched_payment
