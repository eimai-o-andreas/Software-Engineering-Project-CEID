import tkinter as tk
from tkinter import messagebox
from managerAppointment import Room 
from appointment import Appointment
from nurse import Nurse 
from notificationService import NotificationService

class ViewAppointmentScreen:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.selected_appointment = None
        self.displayAppointments()

    def displayAppointments(self):
        self.controller.clear_screen()
        tk.Label(self.root, text="Επιλέξτε ραντεβού για να συνεχίσετε:").pack(pady=10)
        self.appointment_listbox = tk.Listbox(self.root)
        for appt in self.controller.fetchAppointments():
            self.appointment_listbox.insert(tk.END, f"{appt['id']} - {appt['name']}")
        self.appointment_listbox.pack(pady=10)
        tk.Button(self.root, text="Επόμενο", command=self.chooseAppointment).pack(pady=10)

    def chooseAppointment(self):
        try:
            index = self.appointment_listbox.curselection()[0]
            selected = self.controller.fetchAppointments()[index] 
            self.controller.selected_appointment = selected
            self.controller.fetchAvailableRooms()
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε ένα ραντεβού.")

class RoomScreen:
    def __init__(self, root, controller, rooms):
        self.root = root
        self.controller = controller
        self.rooms = rooms
        self.selected_room = None
        self.displayRooms()

    def displayRooms(self):
        self.controller.clear_screen()
        tk.Label(self.root, text="Επιλέξτε δωμάτιο:").pack(pady=10)
        self.room_listbox = tk.Listbox(self.root)
        for room in self.rooms:
            self.room_listbox.insert(tk.END, room)
        self.room_listbox.pack(pady=10)
        tk.Button(self.root, text="Επόμενο", command=self.chooseRoom).pack(pady=10)

    def chooseRoom(self):
        try:
            index = self.room_listbox.curselection()[0]
            selected_room = self.rooms[index]
            self.controller.fetchAvailableNurses(selected_room)
        except IndexError:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε δωμάτιο.")

class ViewNurseScreen:
    def __init__(self, root, controller, nurses):
        self.root = root
        self.controller = controller
        self.nurses = nurses
        self.displayNurses()

    def displayNurses(self):
        self.controller.clear_screen()
        tk.Label(self.root, text="Επιλέξτε νοσηλευτές (πολλαπλή επιλογή):").pack(pady=10)
        self.nurse_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        for nurse in self.nurses:
            self.nurse_listbox.insert(tk.END, nurse)
        self.nurse_listbox.pack(pady=10)
        tk.Button(self.root, text="Ανάθεση", command=self.chooseNurses).pack(pady=10)

    def chooseNurses(self):
        indices = self.nurse_listbox.curselection()
        if not indices:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε τουλάχιστον έναν νοσηλευτή.")
            return
        selected_nurses = [self.nurses[i] for i in indices]
        self.controller.requestConfirmation(selected_nurses)

class ConfirmAssignmentScreen:
    def __init__(self, root, controller, appointment, room, nurses):
        self.root = root
        self.controller = controller
        self.appointment = appointment
        self.room = room
        self.nurses = nurses
        self.displayConfirmScreen()

    def displayConfirmScreen(self):
        self.controller.clear_screen()
        info = (
            f"Επιβεβαιώστε την ανάθεση:\n\n"
            f"Ραντεβού: {self.appointment['name']} (ID: {self.appointment['id']})\n"
            f"Δωμάτιο: {self.room}\n"
            f"Νοσηλευτές: {', '.join(self.nurses)}"
        )
        tk.Label(self.root, text=info, justify=tk.LEFT).pack(pady=10)
        tk.Button(self.root, text="Αποθήκευση", command=lambda: self.confirm(True)).pack(pady=5)
        tk.Button(self.root, text="Απόρριψη", command=lambda: self.confirm(False)).pack(pady=5)

    def confirm(self, answer):
        if answer:
            self.controller.callControllerForSave()
        else:
            self.controller.callControllerForReject()
        self.controller.start()

class NurseNotificationScreen:
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)
        self.controller = controller
        self.root.title("Μη Διαθέσιμοι Νοσηλευτές")
        self.displayNoNursesMessage()

    def displayNoNursesMessage(self):
        tk.Label(self.root, text="Δεν υπάρχουν διαθέσιμοι νοσηλευτές αυτή τη στιγμή.").pack(pady=10)
        tk.Button(self.root, text="Επόμενο", command=lambda:self.controller.notifyParentNoNurses()).pack(pady=10)

class AssignmentWaitingListScreen:
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)
        self.controller = controller
        self.root.title("Λίστα Αναμονής Δωματίου")
        self.displayNoRoomMessage()

    def displayNoRoomMessage(self):
        tk.Label(self.root, text="Δεν υπάρχουν διαθέσιμα δωμάτια.").pack(pady=10)
        tk.Button(self.root, text="Προσθήκη σε λίστα αναμονής", command=self.addToWaitingList).pack(pady=10)
        tk.Button(self.root, text="Άκυρο", command=self.root.destroy).pack(pady=5)

    def addToWaitingList(self):
        self.controller.callWaitingListService()
        messagebox.showinfo("Επιτυχία", "Προστέθηκε στη λίστα αναμονής.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Διαχείριση Ραντεβού")

    appointment_service = Appointment
    room_service = Room()
    nurse_service = Nurse(1, "Maria", "Papadopoulou")
    notification_service = NotificationService()

    from managerAppointment import ManageAppointmentController
    app = ManageAppointmentController(
        root,
        appointment_service,
        room_service,
        nurse_service,
        notification_service
    )
    app.start()
    root.mainloop()
