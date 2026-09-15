class PaymentService():

    def __init__(self, paymentRepo):
        self.paymentRepo = paymentRepo

    def createPayment(self, new_payment):

        if new_payment.id == None:
            raise ValueError("Error in creating payment id")
        
        if new_payment.amount == None:
            raise ValueError("Error in fetching payment amount from booking")
        
        if new_payment.status == None:
            raise ValueError("Error in fetching payment status")
        
        if new_payment.mode == None:
            raise ValueError("Error in fetching payment mode from booking")

        created_payment = self.paymentRepo.createPayment(new_payment)
        return created_payment

    def fetchPayment(self, paymentId):

        if paymentId == None:
            raise ValueError("Payment id required")

        fetched_payment = self.paymentRepo.fetchPayment(paymentId)

        return fetched_payment

    def createPaymentMode(self, new_payment_mode):

        if new_payment_mode.id == None:
            raise ValueError("Payment Mode id required")
        
        if new_payment_mode.added_by == None:
            raise ValueError("User id required")
        
        if new_payment_mode.name == None:
            raise ValueError("Payment Mode name required")

        created_payment_mode = self.paymentRepo.createPaymentMode(new_payment_mode)
        return created_payment_mode

    def fetchPaymentMode(self, payment_modeId):

        if payment_modeId == None:
            raise ValueError("Payment Mode id required")

        fetched_payment_mode = self.paymentRepo.fetchPaymentMode(payment_modeId)

        return fetched_payment_mode
    
    def createPaymentStatusType(self, new_payment_status_type):

        if new_payment_status_type.id == None:
            raise ValueError("Payment Status id required")
        
        if new_payment_status_type.added_by == None:
            raise ValueError("User id required")
        
        if new_payment_status_type.name == None:
            raise ValueError("Payment Status name required")

        created_payment_status_type = self.paymentRepo.createPaymentStatusType(new_payment_status_type)
        return created_payment_status_type

    def fetchPaymentStatusType(self, payment_status_typeId, userId):

        if payment_status_typeId == None:
            raise ValueError("Payment Status Type id required")

        if userId == None:
            raise ValueError("User id required")

        fetched_payment_status_type = self.paymentRepo.fetchPaymentStatusType(payment_status_typeId)

        return fetched_payment_status_type

    def deletePaymentStatusType(self, payment_status_typeId, userId):

        if payment_status_typeId == None:
            raise ValueError("Payment Status Type id required")

        if userId == None:
            raise ValueError("User id required")

        deleted_payment_status_type = self.paymentRepo.deletePaymentStatusType(payment_status_typeId)

        return deleted_payment_status_type

    def updatePaymentStatusType(self, payment_status_typeId, userId):

        if payment_status_typeId == None:
            raise ValueError("Payment Status Type id required")

        if userId == None:
            raise ValueError("User id required")

        updated_payment_status_type = self.paymentRepo.updatePaymentStatusType(payment_status_typeId)

        return updated_payment_status_type
