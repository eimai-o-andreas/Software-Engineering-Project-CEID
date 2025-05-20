import tkinter as tk
from tkinter import messagebox

class PaymentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Πληρωμές και Ιστορικό Λογαριασμών")
        
        # Παράδειγμα λογαριασμών
        self.accounts = {
            "Λογαριασμός 1": 50,
            "Λογαριασμός 2": 75,
            "Λογαριασμός 3": 100
        }

        self.selected_accounts = {}
        self.payment_method = tk.StringVar(value="Κάρτα")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Επιλέξτε Λογαριασμούς για Πληρωμή:").pack()

        for account, amount in self.accounts.items():
            var = tk.BooleanVar()
            self.selected_accounts[account] = var
            tk.Checkbutton(self.root, text=f"{account} - {amount}€", variable=var).pack(anchor='w')

        tk.Label(self.root, text="Επιλέξτε Τρόπο Πληρωμής:").pack(pady=(10,0))
        tk.Radiobutton(self.root, text="Κάρτα", variable=self.payment_method, value="Κάρτα").pack(anchor='w')
        tk.Radiobutton(self.root, text="Μετρητά", variable=self.payment_method, value="Μετρητά").pack(anchor='w')

        tk.Button(self.root, text="Εμφάνιση Ποσού και Επιβεβαίωση", command=self.confirm_payment).pack(pady=10)

    def confirm_payment(self):
        selected = [acc for acc, var in self.selected_accounts.items() if var.get()]
        if not selected:
            messagebox.showwarning("Σφάλμα", "Δεν επιλέξατε κανέναν λογαριασμό.")
            return
        
        total = sum(self.accounts[acc] for acc in selected)
        method = self.payment_method.get()

        confirm = messagebox.askyesno("Επιβεβαίωση", f"Ποσό: {total}€\nΤρόπος Πληρωμής: {method}\n\nΕπιβεβαιώνετε την πληρωμή;")
        if confirm:
            self.execute_payment(selected, total)
        else:
            messagebox.showinfo("Ακύρωση", "Η πληρωμή ακυρώθηκε.")

    def execute_payment(self, selected, total):
        # Προσομοίωση επιτυχούς πληρωμής
        success = True  # Θα μπορούσε να είναι random.choice([True, False]) για προσομοίωση αποτυχίας

        if success:
            for acc in selected:
                del self.accounts[acc]
            messagebox.showinfo("Επιτυχία", f"Η πληρωμή των {total}€ ολοκληρώθηκε με επιτυχία.")
            self.reload_ui()
        else:
            messagebox.showerror("Αποτυχία", "Η πληρωμή απέτυχε. Προσπαθήστε ξανά.")

    def reload_ui(self):
        # Επαναφόρτωση UI
        for widget in self.root.winfo_children():
            widget.destroy()
        self.selected_accounts.clear()
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentSystem(root)
    root.mainloop()
