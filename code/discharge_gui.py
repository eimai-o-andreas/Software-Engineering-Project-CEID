import tkinter as tk
from tkinter import messagebox

class ViewParentScreen(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
                                   
        self.parent_var = tk.StringVar()
        self.parents = self.controller.fetchParents()
        self.displayParents()
    
    def displayParents(self):
        tk.Label(self, text="Επιλογή Γονέα:").pack(pady=10)
        self.parent_var.set(self.parents[0])
        tk.OptionMenu(self, self.parent_var, *self.parents).pack()  

        tk.Button(self, text="Συνέχεια", command=self.chooseParent).pack(pady=20)

    def chooseParent(self):
        selected_parent = self.parent_var.get()
        pending = self.controller.checkForPendingPayments(selected_parent)

        if pending:
            self.controller.foundPending(selected_parent, pending)
        else:
            self.controller.noPending(selected_parent, None)


class ViewPaymentsScreen(tk.Frame):
    def __init__(self, master, parent_name, pending_payments, on_back):
        super().__init__(master)
        self.parent_name = parent_name
        self.pending = pending_payments
        self.on_back = on_back
        self.displayPendingPayments(parent_name)

    def displayPendingPayments(self,parent_name):
        tk.Label(self, text=f"Εκκρεμείς Πληρωμές για {parent_name}", fg="red").pack(pady=10)
        for p in self.pending:
            tk.Label(self, text=f"Πληρωμή ID: {p.id} - Ποσό: {p.cost}€").pack()

        tk.Button(self, text="Πίσω", command=self.on_back).pack(pady=20)

class DischargeScreen(tk.Frame):
    def __init__(self, master, controller, parent_name, on_done):
        super().__init__(master)
        self.controller = controller
        self.parent_name = parent_name
        self.on_done = on_done
        self.displayDischargeScreen(parent_name)

    def displayDischargeScreen(self,parent_name):
        tk.Label(self, text=f"Έκδοση εξιτηρίου για {parent_name}").pack(pady=10)
        tk.Button(self, text="Έκδοση", command=self.issueDischarge).pack(pady=20)

    def issueDischarge(self):
        self.controller.callControllerForDischarge(self.parent_name)
        messagebox.showinfo("Επιτυχία", f"Εκδόθηκε εξιτήριο για τον {self.parent_name}")
        self.on_done()


