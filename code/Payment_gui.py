import tkinter as tk
from paymentController import PaymentController
from tkinter import messagebox
from payment import Payment

class ViewBillsScreen:
    def __init__(self, master, parent_id):
        self.master = master
        self.controller = PaymentController(parent_id, master)
        self.bills = self.controller.fetchPendingBills()
        self.selected = []
        self.displayBills() 

    def displayBills(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Εκκρεμείς Λογαριασμοί").pack()
        self.bill_vars = {}

        for bill in self.bills:
            var = tk.IntVar()
            cb = tk.Checkbutton(self.frame, text=f"Λογαριασμός {bill.id}: {bill.cost}€", variable=var)
            cb.pack(anchor='w')
            self.bill_vars[bill.id] = var

        tk.Button(self.frame, text="Συνέχεια", command=self.selectBills).pack(pady=10)

    def selectBills(self):
        selected_ids = [bid for bid, var in self.bill_vars.items() if var.get() == 1]
        self.controller.sendSelectedBills(selected_ids) 
  
    @staticmethod
    def redirectToBills(master, parent_id):
        ViewBillsScreen(master, parent_id)


    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

class ViewAmountScreen:
    def __init__(self, master, controller, amount):
        self.root = master
        self.controller = controller
        self.amount = amount
        self.payment_method = tk.StringVar()
        self.displayAmount()

    def displayAmount(self):
        self.clear()

        tk.Label(self.root, text=f"Συνολικό ποσό προς πληρωμή: {self.amount}€", font=("Helvetica", 14)).pack(pady=10)

        tk.Label(self.root, text="Επιλέξτε Τρόπο Πληρωμής:", font=("Helvetica", 12)).pack(pady=(10, 0))
        tk.Radiobutton(self.root, text="Κάρτα", variable=self.payment_method, value="Κάρτα").pack(anchor='w', padx=20)
        tk.Radiobutton(self.root, text="Μετρητά", variable=self.payment_method, value="Μετρητά").pack(anchor='w', padx=20)

        tk.Button(self.root, text="Επιβεβαίωση", command=self.save).pack(pady=15)

    def save(self):
        method = self.payment_method.get()
        if not method:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε τρόπο πληρωμής.")
            return
        print(f"[Controller] Επιλέχθηκε τρόπος πληρωμής: {method}")
        self.controller.payment_method = method
        self.controller.requestConfirmation(self.amount)
   
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    @staticmethod
    def redirectToAmount(master, controller, amount):
        ViewAmountScreen(master, controller, amount)

class Confirm2Screen:
    def __init__(self, controller, parent_id, amount, method):
        self.controller = controller
        self.parent_id = parent_id
        self.amount = amount
        self.method = method
        self.display()

    def display(self):
        confirmation = messagebox.askokcancel(
            "Επιβεβαίωση Πληρωμής",
            f"Πρόκειται να πληρώσετε {self.amount}€ με {self.method}.\nΘέλετε να συνεχίσετε;"
        )
        if confirmation:
            self.confirmPayment()

    def confirmPayment(self):
        print("[Confirm] Επιβεβαιώθηκε η πληρωμή.")
        self.controller.processPayment()

class RetryMessScreen:
    def __init__(self, master, controller, amount):
        self.master = master
        self.controller = controller
        self.amount = amount
        self.showRetryMessage()

    def showRetryMessage(self):
        self.window = tk.Toplevel(self.master)
        self.window.title("Αποτυχία Πληρωμής")

        tk.Label(self.window, text="Η πληρωμή απέτυχε. Θέλετε να προσπαθήσετε ξανά;", font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.window, text="Ναι", command=lambda: ViewAmountScreen.redirectToAmount(self.master, self.controller, self.amount)).pack(side='left', padx=20, pady=20)
        tk.Button(self.window, text="Όχι", command=lambda: ViewBillsScreen.redirectToBills(self.master, self.controller.parent_id)).pack(side='right', padx=20, pady=20)

    
       

#Main to test use case 2 : parent payments
def seed_mock_data():
    Payment(parent=1, cost=20.0)
    Payment(parent=1, cost=35.5)
    Payment(parent=1, cost=50.0)
    paid_payment = Payment(parent=1, cost=15.0)

def main():
    seed_mock_data()
    root = tk.Tk()
    root.title("Πληρωμές Γονέα")
    app = ViewBillsScreen(root, parent_id=1)
    root.mainloop()

if __name__ == "__main__":
    main()

