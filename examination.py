import tkinter as tk
from tkinter import messagebox

class ExaminationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Ανάθεση Ιατρικών Εξετάσεων")

        self.all_exams = {
            "Αιματολογική": 25,
            "Ακτινογραφία": 50,
            "Μαγνητική": 200,
            "Τεστ COVID": 30,
            "Ουρολογική": 40
        }
        self.already_scheduled = {"Μαγνητική"}  # Ήδη προγραμματισμένες
        self.exam_vars = {}

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Επιλογή Εξετάσεων:").pack(pady=5)

        for exam in self.all_exams:
            var = tk.IntVar()
            self.exam_vars[exam] = var
            cb = tk.Checkbutton(self.root, text=f"{exam} ({self.all_exams[exam]}€)", variable=var)
            cb.pack(anchor="w")

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Έλεγχος & Αποθήκευση", command=self.check_and_save).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Ακύρωση", command=self.cancel_action).grid(row=0, column=1, padx=5)

    def check_and_save(self):
        selected_exams = [exam for exam, var in self.exam_vars.items() if var.get() == 1]

        if not selected_exams:
            # Εναλλακτική Ροή 2: Δεν έγινε αποθήκευση
            messagebox.showerror("Αποτυχία", "Δεν επιλέχθηκαν εξετάσεις. Η αποθήκευση απέτυχε.")
            return

        already_selected = [exam for exam in selected_exams if exam in self.already_scheduled]

        if already_selected:
            # Εναλλακτική Ροή 1: Υπάρχουν ήδη προγραμματισμένες
            msg = "Οι παρακάτω εξετάσεις είναι ήδη προγραμματισμένες:\n"
            msg += "\n".join(already_selected)
            messagebox.showwarning("Προγραμματισμένες Εξετάσεις", msg)
            return  # Επιστροφή στο βήμα 3

        # Βασική Ροή: Επιτυχής αποθήκευση
        total_cost = sum(self.all_exams[exam] for exam in selected_exams)
        self.save_examinations(selected_exams, total_cost)

    def save_examinations(self, exams, cost):
        messagebox.showinfo("Αποθήκευση", f"Οι εξετάσεις αποθηκεύτηκαν επιτυχώς.\nΣυνολικό Κόστος: {cost}€")
        print(f"Νέες εξετάσεις: {exams}")
        print(f"Ενημέρωση φακέλου γονέα με κόστος: {cost}€")
        print("Αποστολή μηνύματος στον γονέα για τις νέες εξετάσεις...")

        # Reset επιλογές
        for var in self.exam_vars.values():
            var.set(0)

    def cancel_action(self):
        response = messagebox.askyesno("Ακύρωση", "Είστε σίγουρος ότι θέλετε να ακυρώσετε;")
        if response:
            messagebox.showinfo("Ακύρωση", "Η διαδικασία ακυρώθηκε.")
            for var in self.exam_vars.values():
                var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExaminationSystem(root)
    root.mainloop()
