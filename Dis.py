

import tkinter as tk
from tkinter import messagebox

class DischargeSystem:
    def init(self, root):
        self.root = root
        self.root.title("Σύστημα Έκδοσης Εξιτηρίου")

        self.parents = ["Γονέας 1", "Γονέας 2", "Γονέας 3"]
        self.accounts = {"Γονέας 1": 0, "Γονέας 2": 1, "Γονέας 3": 0}  # 0=no pending, 1=pending

        self.create_widgets()

    def create_widgets(self):
        # Επιλογή γονέα
        tk.Label(self.root, text="Επιλογή Γονέα:").pack()
        self.selected_parent = tk.StringVar(self.root)
        self.selected_parent.set(self.parents[0])
        tk.OptionMenu(self.root, self.selected_parent, *self.parents).pack()

        # Κουμπί έκδοσης εξιτηρίου
        tk.Button(self.root, text="Έκδοση Εξιτηρίου", command=self.issue_discharge).pack(pady=10)

    def issue_discharge(self):
        parent = self.selected_parent.get()
        has_pending = self.accounts[parent]

        if has_pending:
            self.show_pending_accounts()
        else:
            self.send_message_and_update()
            messagebox.showinfo("Επιτυχία", f"Ο γονέας '{parent}' έλαβε το εξιτήριο.\nΤο δωμάτιο ενημερώθηκε ως ελεύθερο.")

    def show_pending_accounts(self):
        messagebox.showwarning("Εκκρεμείς Λογαριασμοί", "Ο γονέας έχει εκκρεμείς λογαριασμούς.\nΔεν είναι δυνατή η έκδοση εξιτηρίου.")

    def send_message_and_update(self):
        # Θα προσθέταμε εδώ σύνδεση με backend ή αποστολή email
        print("Αποστολή μηνύματος σε γονέα, θεράποντα, νοσηλευτές...")
        print("Ενημέρωση δωματίου ως ελεύθερο...")

if name == "main":
    root = tk.Tk()
    app = DischargeSystem(root)
    root.mainloop()



