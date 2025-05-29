import tkinter as tk
from tkinter import messagebox
from notificationService import NotificationService
from seminars import Seminar
from seminarParticipants import SeminarParticipants

class NotificationWaitList:
    def __init__(self):
        self.wait_list = []

    def addToList(self, parent_id):
        self.wait_list.append(parent_id)
        print(f"Γονέας {parent_id}: Μπήκατε στην λίστα ενημέρωσης")

class BookSeminarController:
    def __init__(self, master):
        self.master = master
        self.participants = SeminarParticipants()
        self.wait_list = NotificationWaitList()
        self.notification_service = NotificationService()
        self.parent_id = 1
        self.selected_seminar = None
        
         # === Εισαγωγή dummy δεδομένων ===
        if not Seminar.seminars:  # Για να μην ξαναφορτώνονται σε κάθε run
            from datetime import datetime
            Seminar.seminars.append(Seminar(
                title="Σεμινάριο Διατροφής",
                description="Συμβουλές διατροφής για νέους γονείς.",
                audience="Γονείς",
                speakerName="Δρ. Δημητρίου",
                room="Αίθουσα 1",
                datetime=datetime.strptime("2025-04-30 10:00", "%Y-%m-%d %H:%M")
            ))
            Seminar.seminars.append(Seminar(
                title="Ψυχολογία Παιδιού",
                description="Κατανόηση της συμπεριφοράς των παιδιών.",
                audience="Γονείς & Εκπαιδευτικοί",
                speakerName="Δρ. Σταυρίδη",
                room="Αίθουσα 2",
                datetime=datetime.strptime("2025-05-01 09:00", "%Y-%m-%d %H:%M")
            ))
            Seminar.seminars.append(Seminar(
                title="Πρώτες Βοήθειες για Παιδιά",
                description="Βασικές γνώσεις πρώτων βοηθειών για παιδιά.",
                audience="Όλοι",
                speakerName="Δρ. Παπά",
                room="Αίθουσα 1",
                datetime=datetime.strptime("2025-05-01 11:00", "%Y-%m-%d %H:%M")
            ))

        self.start()

    def start(self):
        seminars = Seminar.getSeminarList()
        if not seminars:
            from parentSeminar_gui import FMessage3Screen
            FMessage3Screen(self, self.master)
        else:
            from parentSeminar_gui import ViewSeminarScreen
            ViewSeminarScreen(self, self.master, seminars)

    def fetchSeminarDetails(self, seminar):
        self.selected_seminar = seminar
        details = Seminar.getSeminarDetails(seminar)
        from parentSeminar_gui import ViewSeminarDetailsScreen
        ViewSeminarDetailsScreen(self, self.master, details)

    def checkAvailability(self):
        available = Seminar.getAvailability(self.selected_seminar)
        if available:
            from parentSeminar_gui import Confirm3Screen
            Confirm3Screen(self, self.master, self.selected_seminar)
        else:
            messagebox.showinfo("Πλήρες", "Το σεμινάριο είναι πλήρες.")
            self.start()

    def actOnParticipation(self):
        added = self.participants.updateParticipantList(self.selected_seminar, self.parent_id)
        if added:
            self.selected_seminar.updateAvailability()
        else:
            messagebox.showinfo("Πλήρες", "Tο σεμινάριο είναι πλήρες.")
        self.start()

    def addToNotificationWaitList(self):
        self.wait_list.addToList(self.parent_id)

    def checkForNewSeminars(self):
        self.notification_service.notifyParent(self.parent_id)
        messagebox.showinfo("Ενημέρωση", "Θα ειδοποιηθείτε για νέα σεμινάρια.")
        self.start()

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()

# === Main App ===
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Σύστημα Σεμιναρίων")
    app = BookSeminarController(root)
    root.mainloop()
