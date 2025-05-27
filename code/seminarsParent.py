import tkinter as tk
from tkinter import messagebox

class SeminarManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Συμμετοχή σε Σεμινάρια")

        # Προσωρινές λίστες για τα δεδομένα
        self.seminars = [
            {"id": 1, "title": "Σεμινάριο 1", "date": "2025-05-10", "details": "Θεματικές ενότητες: Πρώτες βοήθειες, Ομιλητής: Δρ. Παπαδόπουλος"},
            {"id": 2, "title": "Σεμινάριο 2", "date": "2025-05-20", "details": "Θεματικές ενότητες: Ψυχολογία παιδιών, Ομιλητής: Δρ. Σταμάτη"},
            {"id": 3, "title": "Σεμινάριο 3", "date": "2025-06-01", "details": "Θεματικές ενότητες: Δικαιώματα παιδιών, Ομιλητής: Δρ. Νικολάου"}
        ]
        self.participants = []  # Κατάλογος συμμετεχόντων
        self.waiting_list = []  # Λίστα αναμονής για σεμινάρια
        self.selected_seminar = None
        
        # Δημιουργία αρχικής οθόνης
        self.create_seminar_list_screen()

    def create_seminar_list_screen(self):
        """Οθόνη για την εμφάνιση διαθέσιμων σεμιναρίων"""
        self.clear_screen()

        tk.Label(self.root, text="Διαθέσιμα Σεμινάρια:").pack()
        self.seminar_listbox = tk.Listbox(self.root)
        for seminar in self.seminars:
            self.seminar_listbox.insert(tk.END, f"{seminar['title']} - {seminar['date']}")
        self.seminar_listbox.pack(pady=10)

        tk.Button(self.root, text="Επόμενο", command=self.select_seminar).pack(pady=10)
        
        # Αν δεν υπάρχουν σεμινάρια
        if not self.seminars:
            tk.Button(self.root, text="Ενημέρωσέ με για νέα σεμινάρια", command=self.notify_new_seminars).pack(pady=10)

    def select_seminar(self):
        """Επιλογή σεμιναρίου και εμφάνιση λεπτομερειών"""
        try:
            selected_index = self.seminar_listbox.curselection()[0]
            self.selected_seminar = self.seminars[selected_index]
            self.create_seminar_details_screen()
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε ένα σεμινάριο.")

    def create_seminar_details_screen(self):
        """Οθόνη για την εμφάνιση πληροφοριών σεμιναρίου και δήλωση συμμετοχής"""
        self.clear_screen()

        tk.Label(self.root, text=f"Πληροφορίες για το σεμινάριο: {self.selected_seminar['title']}").pack()
        tk.Label(self.root, text=f"Ημερομηνία: {self.selected_seminar['date']}").pack()
        tk.Label(self.root, text=f"Λεπτομέρειες: {self.selected_seminar['details']}").pack()

        tk.Button(self.root, text="Δηλώστε Συμμετοχή", command=self.confirm_participation).pack(pady=10)
        tk.Button(self.root, text="Επιστροφή", command=self.create_seminar_list_screen).pack(pady=10)

    def confirm_participation(self):
        """Οθόνη επιβεβαίωσης συμμετοχής"""
        self.clear_screen()

        tk.Label(self.root, text="Είστε σίγουροι ότι θέλετε να δηλώσετε συμμετοχή στο σεμινάριο;").pack()
        
        tk.Button(self.root, text="Ναι", command=self.register_participation).pack(pady=10)
        tk.Button(self.root, text="Όχι", command=self.create_seminar_list_screen).pack(pady=10)

    def register_participation(self):
        """Καταχώριση συμμετοχής στο σεμινάριο"""
        self.participants.append(self.selected_seminar)
        messagebox.showinfo("Επιτυχία", f"Επιτυχής δήλωση συμμετοχής στο σεμινάριο: {self.selected_seminar['title']}.")

        # Ενημέρωση πληρότητας του σεμιναρίου
        self.seminars.remove(self.selected_seminar)

        # Ειδοποίηση στον γονέα με τις πληροφορίες του σεμιναρίου
        messagebox.showinfo("Ειδοποίηση", f"Θα λάβετε περισσότερες πληροφορίες για το σεμινάριο {self.selected_seminar['title']}.")

        # Επιστροφή στην οθόνη σεμιναρίων
        self.create_seminar_list_screen()

    def notify_new_seminars(self):
        """Ενημέρωση γονέα για νέα σεμινάρια"""
        messagebox.showinfo("Ενημέρωση", "Θα ειδοποιηθείτε μόλις υπάρχουν νέα διαθέσιμα σεμινάρια.")
        self.waiting_list.append(self.selected_seminar)
        self.create_seminar_list_screen()

    def clear_screen(self):
        """Καθαρίζει την οθόνη"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SeminarManagementSystem(root)
    root.mainloop()
