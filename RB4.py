import tkinter as tk
from tkinter import messagebox

class RoomManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Διαχείριση Δωματίων")

        # Προσωρινές λίστες για τα δεδομένα
        self.appointments = [
            {"id": 1, "name": "Ραντεβού 1", "status": "accepted"},
            {"id": 2, "name": "Ραντεβού 2", "status": "accepted"},
            {"id": 3, "name": "Ραντεβού 3", "status": "accepted"}
        ]
        self.rooms = ["Δωμάτιο 1", "Δωμάτιο 2", "Δωμάτιο 3", "Δωμάτιο 4"]
        self.nurses = ["Νοσηλευτής 1", "Νοσηλευτής 2", "Νοσηλευτής 3", "Νοσηλευτής 4"]
        
        # Δημιουργία αρχικής οθόνης
        self.create_appointments_screen()

    def create_appointments_screen(self):
        """Οθόνη για την επιλογή ραντεβού"""
        self.clear_screen()

        tk.Label(self.root, text="Επιλέξτε ραντεβού για να αναθέσετε δωμάτιο και νοσηλευτικό προσωπικό:").pack()
        self.appointment_listbox = tk.Listbox(self.root)
        for appointment in self.appointments:
            self.appointment_listbox.insert(tk.END, f"{appointment['id']} - {appointment['name']}")
        self.appointment_listbox.pack(pady=10)

        tk.Button(self.root, text="Επόμενο", command=self.select_appointment).pack(pady=10)

    def select_appointment(self):
        """Επιλογή ραντεβού και μετά πηγαίνουμε στην οθόνη δωμάτιων"""
        try:
            self.selected_appointment_index = self.appointment_listbox.curselection()[0]
            self.selected_appointment = self.appointments[self.selected_appointment_index]
            self.create_rooms_screen()
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε ένα ραντεβού.")

    def create_rooms_screen(self):
        """Οθόνη για την επιλογή δωμάτιου"""
        self.clear_screen()

        tk.Label(self.root, text="Επιλέξτε δωμάτιο:").pack()
        self.room_listbox = tk.Listbox(self.root)
        for room in self.rooms:
            self.room_listbox.insert(tk.END, room)
        self.room_listbox.pack(pady=10)

        tk.Button(self.root, text="Επόμενο", command=self.select_room).pack(pady=10)

    def select_room(self):
        """Επιλογή δωμάτιου και μετά πηγαίνουμε στην οθόνη νοσηλευτών"""
        try:
            self.selected_room_index = self.room_listbox.curselection()[0]
            self.selected_room = self.rooms[self.selected_room_index]
            self.create_nurses_screen()
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε δωμάτιο.")

    def create_nurses_screen(self):
        """Οθόνη για την επιλογή νοσηλευτών"""
        self.clear_screen()

        tk.Label(self.root, text="Επιλέξτε νοσηλευτές:").pack()
        self.nurse_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        for nurse in self.nurses:
            self.nurse_listbox.insert(tk.END, nurse)
        self.nurse_listbox.pack(pady=10)

        tk.Button(self.root, text="Ανάθεση", command=self.assign_room_and_nurse).pack(pady=10)

    def assign_room_and_nurse(self):
        """Ανάθεση δωμάτιου και νοσηλευτών στο ραντεβού"""
        try:
            # Επιλογή νοσηλευτών
            selected_nurses_indexes = self.nurse_listbox.curselection()
            selected_nurses = [self.nurses[i] for i in selected_nurses_indexes]

            # Ανάθεση δωμάτιου και νοσηλευτών
            message = f"Το ραντεβού με ID {self.selected_appointment['id']} και όνομα {self.selected_appointment['name']} ορίστηκε στο δωμάτιο {self.selected_room}.\n"
            message += f"Ανατέθηκαν οι νοσηλευτές: {', '.join(selected_nurses)}."
            messagebox.showinfo("Επιτυχία", message)

            # Ενημέρωση των ραντεβού, δωματίων και νοσηλευτών
            self.rooms.pop(self.selected_room_index)
            self.nurses = [nurse for i, nurse in enumerate(self.nurses) if i not in selected_nurses_indexes]

            # Ενημέρωση του ραντεβού
            self.appointments[self.selected_appointment_index]['status'] = 'assigned'

            # Επιστροφή στην αρχική οθόνη
            self.root.quit()

        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε τουλάχιστον έναν νοσηλευτή.")

    def clear_screen(self):
        """Καθαρίζει την οθόνη"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoomManagementSystem(root)
    root.mainloop()