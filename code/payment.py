from exam import Exam  

class Payment:
    next_id = 1
    all_payments = [] 

    def __init__(self, parent, examination=None, cost=0.0, status="unpaid", id=None):
        if id is None:
            self.id = Payment.next_id
            Payment.next_id += 1
        else:
            self.id = id 

        self.parent = parent   
        self.examination = examination  
        self.cost = cost                 
        self.status = status           

        Payment.all_payments.append(self)

    @staticmethod
    def addNewPayment(parent, examination, cost):
        print(f"[Payment] Νέα πληρωμή προστέθηκε: {cost}€")
        return Payment(parent, examination, cost)

    @staticmethod
    def getBills(parent_id):
        return [p for p in Payment.all_payments if p.parent == parent_id and p.status == "unpaid"]
    
    @staticmethod
    def getAmount(bills):
        return [b.cost for b in bills]

    @staticmethod
    def updateStatus(payments):
        for p in payments:
            p.status = "paid"
        print("Η πληρωμή ολοκληρώθηκε επιτυχώς.")
