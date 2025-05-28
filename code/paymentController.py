from payment import Payment
from notificationService import NotificationService
from tkinter import messagebox

class PaymentController:
    def __init__(self, parent_id, master):
        self.parent_id = parent_id
        self.master = master
        self.selected_bills = []

    def fetchPendingBills(self):
        return Payment.getBills(self.parent_id)

    def sendSelectedBills(self, bill_ids): #
        self.selected_bills = [b for b in Payment.getBills(self.parent_id) if b.id in bill_ids]
        self.checkNumberOfSelectedBills()

    def checkNumberOfSelectedBills(self):
        from payment_gui import ViewAmountScreen
        if len(self.selected_bills) > 1:
            self.addAmount()
            self.view_amount_screen = ViewAmountScreen(self.master, self, self.total_amount)
        elif len(self.selected_bills) == 1:
            amount = self.selected_bills[0].cost
            self.view_amount_screen = ViewAmountScreen(self.master, self, amount)            

    def addAmount(self):
        self.total_amount = sum(Payment.getAmount(self.selected_bills))

    def requestConfirmation(self, amount):
        from payment_gui import Confirm2Screen
        Confirm2Screen(self, self.parent_id, amount, self.payment_method)
    
    def processPayment(self):
        fail_pass = True  # αλλαγή το χειροκίνητα σε False για να προσομοιώσεις αποτυχία
    
        if fail_pass:
            Payment.updateStatus(self.selected_bills)
            NotificationService.sendSuccessMessage(self.parent_id)
            messagebox.showinfo("Επιτυχία", "Η πληρωμή ολοκληρώθηκε επιτυχώς.")
        else:
            from payment_gui import RetryMessScreen
            amount = self.selected_bills[0].cost if len(self.selected_bills) == 1 else self.total_amount
            self.retry_screen = RetryMessScreen(self.master, self, amount)
