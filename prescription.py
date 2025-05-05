import tkinter as tk
from tkinter import messagebox

class PrescriptionSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Συνταγογράφηση Φαρμάκων")

        self.medicines = ["Παρακεταμόλη", "Αμοξικιλλίνη", "Ιβουπροφαίνη", "Κετοπροφαίνη"]

        self.create_widgets()

    def create_widgets(self):
        # Οθόνη εμφάνισης φαρμάκων
        tk.Label(self.root, text="Επιλογή Φαρμάκου:").pack(pady=5)
        self.selected_medicine = tk.StringVar(self.root)
        self.selected_medicine.set(self.medicines[0])
        tk.OptionMenu(self.root, self.selected_medicine, *self.medicines).pack()

        # Εισαγωγή δοσολογίας
        tk.Label(self.root, text="Δοσολογία:").pack(pady=5)
        self.dosage_entry = tk.Entry(self.root)
        self.dosage_entry.pack()

        # Κουμπιά δράσεων
        action_frame = tk.Frame(self.root)
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Αποθήκευση Συνταγής", command=self.save_prescription).grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Ακύρωση", command=self.cancel_prescription).grid(row=0, column=1, padx=5)

    def save_prescription(self):
        medicine = self.selected_medicine.get()
        dosage = self.dosage_entry.get().strip()

        # Εναλλακτική Ροή 1: Δοσολογία δεν έχει εισαχθεί
        if not dosage:
            messagebox.showerror("Αποτυχία", "Δεν έχει εισαχθεί δοσολογία.\nΕπιστροφή στην οθόνη εμφάνισης φαρμάκων.")
            return

        # Βασική Ροή: Επιτυχής αποθήκευση
        messagebox.showinfo("Αποθήκευση Συνταγής", f"Η συνταγή για {medicine} με δοσολογία '{dosage}' αποθηκεύτηκε.")
        print(f"Καταγραφή: Φάρμακο: {medicine}, Δοσολογία: {dosage}")
        self.update_medical_record(medicine, dosage)

    def cancel_prescription(self):
        # Εναλλακτική Ροή 2: Επιβεβαίωση ακύρωσης
        response = messagebox.askyesno("Επιβεβαίωση Ακύρωσης", "Είστε σίγουρος ότι θέλετε να ακυρώσετε τη συνταγή;\nΗ συνταγή δεν θα αποθηκευτεί.")
        if response:
            self.dosage_entry.delete(0, tk.END)
            self.selected_medicine.set(self.medicines[0])
            messagebox.showinfo("Ακύρωση", "Η συνταγή ακυρώθηκε.\nΕπιστροφή στην οθόνη εμφάνισης φαρμάκων.")

    def update_medical_record(self, medicine, dosage):
        print("Ενημέρωση ιατρικού φακέλου του γονέα...")
        print("Αποστολή μηνύματος στον γονέα: Δημιουργήθηκε νέα συνταγή.")
        # Πιθανή επέκταση: αποστολή email, ενημέρωση σε βάση δεδομένων, API call κλπ

if __name__ == "__main__":
    root = tk.Tk()
    app = PrescriptionSystem(root)
    root.mainloop()
