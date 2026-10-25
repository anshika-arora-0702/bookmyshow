from models.domain.payments.payment import Payment as PaymentDomain
from models.database.payments.payment import Payment as PaymentDB
from models.database.payments.payment_status import PaymentStatus

from datetime import datetime, timezone

from exceptions.payment_exceptions import PaymentException

class PaymentRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    def _payment_to_db(self,payment:PaymentDomain) -> PaymentDB:

        return PaymentDB(id = payment.id, 
                      amount = payment.amount, 
                      mode = payment.mode,  
                      status = payment.status,
                      created_at = datetime.now(timezone.utc),
                      updated_at = datetime.now(timezone.utc)
                      )
    
    def _payment_to_domain(self,payment:PaymentDB) -> PaymentDomain:

        return PaymentDomain(id = payment.id, 
                      amount = payment.amount, 
                      mode = payment.mode,  
                      status = payment.status
                      )

    def createPendingPayment(self, new_payment):

        try:
            payment_db = self._payment_to_db(new_payment)
            self.db_session.add(payment_db)
            self.db_session.flush()
            return self._payment_to_domain(payment_db)

        except Exception :
            raise PaymentException()

    def markSuccessful(self, payment_id): 

        try:
            payment:PaymentDB = self.db_session.get(PaymentDB, payment_id)
            payment.status = PaymentStatus.SUCCESSFUL
            payment.updated_at = datetime.now(timezone.utc)
            self.db_session.flush()

        except:
            raise PaymentException()
        
    def markFailed(self, payment_id):

        try:
            payment : PaymentDB= self.db_session.get(PaymentDB, payment_id)
            payment.status = PaymentStatus.FAILED
            payment.updated_at = datetime.now(timezone.utc)
            self.db_session.flush()

        except:
            raise PaymentException()
        
    def markUnknown(self, payment_id):

        try:
            payment : PaymentDB= self.db_session.get(PaymentDB, payment_id)
            payment.status = PaymentStatus.UNKNOWN
            payment.updated_at = datetime.now(timezone.utc)
            self.db_session.flush()

        except:
            raise PaymentException()