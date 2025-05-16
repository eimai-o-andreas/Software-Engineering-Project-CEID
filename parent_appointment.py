import tkinter as tk
from tkinter import messagebox

class AppointmentBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Προγραμματισμός Ραντεβού για Μαιευτήριο")

        # Δεδομένα για ιατρούς και ραντεβού
        self.doctors = {
            "Μαιευτήρες": ["Δρ. Κωνσταντίνος Παπαδόπουλος", "Δρ. Μαρία Σταμάτη"],
            "Γυναικολόγοι": ["Δρ. Νικόλαος Μαραγκός", "Δρ. Άννα Δημητρίου"]
        }
        self.available_times = {
            "Δρ. Κωνσταντίνος Παπαδόπουλος": ["2025-05-01 09:00", "2025-05-01 14:00"],
            "Δρ. Μαρία Σταμάτη": ["2025-05-02 10:00", "2025-05-02 16:00"],
            "Δρ. Νικόλαος Μαραγκός": ["2025-05-03 11:00", "2025-05-03 15:00"],
            "Δρ. Άννα Δημητρίου": ["2025-05-04 12:00", "2025-05-04 17:00"]
        }

        self.selected_doctor = None
        self.selected_time = None

        # Δημιουργία αρχικής οθόνης
        self.create_category_screen()

    def create_category_screen(self):
        """Οθόνη για την επιλογή κατηγορίας θεραπόντων (Μαιευτήρες, Γυναικολόγοι)"""
        self.clear_screen()
        tk.Label(self.root, text="Επιλέξτε κατηγορία γιατρού:").pack(pady=10)

        self.category_var = tk.StringVar(value="Μαιευτήρες")
        tk.Radiobutton(self.root, text="Μαιευτήρες", variable=self.category_var, value="Μαιευτήρες", command=self.load_doctors).pack(pady=5)
        tk.Radiobutton(self.root, text="Γυναικολόγοι", variable=self.category_var, value="Γυναικολόγοι", command=self.load_doctors).pack(pady=5)

        tk.Button(self.root, text="Επόμενο", command=self.select_doctor_screen).pack(pady=10)

    def load_doctors(self):
        """Φορτώνει τους ιατρούς ανά κατηγορία"""
        self.selected_doctor = None
        self.selected_time = None
        self.create_doctor_screen()

    def create_doctor_screen(self):
        """Οθόνη για την επιλογή ιατρού"""
        self.clear_screen()
        category = self.category_var.get()

        tk.Label(self.root, text=f"Επιλέξτε Ιατρό από την κατηγορία {category}:").pack(pady=10)

        self.doctor_listbox = tk.Listbox(self.root)
        for doctor in self.doctors[category]:
            self.doctor_listbox.insert(tk.END, doctor)
        self.doctor_listbox.pack(pady=10)

        tk.Button(self.root, text="Επόμενο", command=self.select_doctor_screen).pack(pady=10)

    def select_doctor_screen(self):
        """Επιλογή ιατρού από τη λίστα"""
        try:
            selected_index = self.doctor_listbox.curselection()[0]
            self.selected_doctor = self.doctors[self.category_var.get()][selected_index]
            self.create_time_screen()
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε έναν ιατρό.")

    def create_time_screen(self):
        """Οθόνη για την επιλογή ημερομηνίας και ώρας"""
        self.clear_screen()

        tk.Label(self.root, text=f"Επιλέξτε Ημερομηνία και Ώρα για τον {self.selected_doctor}:").pack(pady=10)

        self.time_listbox = tk.Listbox(self.root)
        for time in self.available_times[self.selected_doctor]:
            self.time_listbox.insert(tk.END, time)
        self.time_listbox.pack(pady=10)

        tk.Button(self.root, text="Επόμενο", command=self.select_time_screen).pack(pady=10)

    def select_time_screen(self):
        """Επιλογή ώρας από τη λίστα"""
        try:
            selected_index = self.time_listbox.curselection()[0]
            self.selected_time = self.available_times[self.selected_doctor][selected_index]
            self.create_confirm_screen()
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε μια ώρα.")

    def create_confirm_screen(self):
        """Οθόνη επιβεβαίωσης ραντεβού"""
        self.clear_screen()

        tk.Label(self.root, text=f"Επιλέξατε ραντεβού με τον {self.selected_doctor} στις {self.selected_time}").pack(pady=10)

        tk.Button(self.root, text="Επιβεβαίωση", command=self.confirm_appointment).pack(pady=10)
        tk.Button(self.root, text="Ακύρωση", command=self.create_category_screen).pack(pady=10)

    def confirm_appointment(self):
        """Καταχώρηση ραντεβού και αποστολή ειδοποίησης"""
        messagebox.showinfo("Επιτυχία", f"Το ραντεβού με τον {self.selected_doctor} στις {self.selected_time} καταχωρήθηκε με επιτυχία.")

        # Ενημέρωση διαθεσιμότητας
        self.available_times[self.selected_doctor].remove(self.selected_time)

        # Αποστολή ειδοποίησης στον ιατρό
        messagebox.showinfo("Ειδοποίηση", f"Ο {self.selected_doctor} ειδοποιήθηκε για το νέο ραντεβού.")

        # Επιστροφή στην οθόνη κράτησης ραντεβού
        self.create_category_screen()

    def clear_screen(self):
        """Καθαρίζει την οθόνη"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentBookingSystem(root)
    root.mainloop()