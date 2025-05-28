from parent import parent 
from payment import Payment
from discharge import Discharge
from notificationService import NotificationService
from nurse import Nurse
from room import Room

class DischargeController:
    def __init__(self, root):
        self.root = root
        self.notification_service = NotificationService()
        self.nurse = Nurse(1, "Νοσηλευτής", "Γιώργος")
        self.room = Room()
        self.start()

    def start(self):
        from discharge_gui import ViewParentScreen
        self.current_screen = ViewParentScreen(self.root, self)
        self.current_screen.pack(fill="both", expand=True)

    def fetchParents(self):
        return list(parent.keys())

    def checkForPendingPayments(self, parent_name):
        selected_parent = parent[parent_name]
        return Payment.getBills(selected_parent)

    def foundPending(self, parent_name, pending):
        self.clear_screen()
        from discharge_gui import ViewPaymentsScreen
        screen = ViewPaymentsScreen(self.root, parent_name, pending, self.start)
        screen.pack(fill="both", expand=True)
        self.current_screen = screen

    def noPending(self, parent_name, _):
        self.clear_screen()
        from discharge_gui import DischargeScreen
        screen = DischargeScreen(self.root, self, parent_name, self.start)
        screen.pack(fill="both", expand=True)
        self.current_screen = screen

    def callControllerForDischarge(self, parent_name):
        selected_parent = parent[parent_name]
        Discharge.createDischarge(selected_parent)

        # Ειδοποιήσεις
        self.notification_service.notifyDoctor(selected_parent.id)
        self.notification_service.notifyParentDischarge(selected_parent.id)
        self.notification_service.notifyNurse(selected_parent.id)
        self.notification_service.sendSuccessMessage(selected_parent.id)

        # Ενημέρωση Διαθεσιμότητας
        self.nurse.updateAvailableNurses(["Νοσηλευτής 1"])
        self.room.updateRoomAsAvailable("Δωμάτιο 1")

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("Έκδοση Εξιτηρίου")
    #Για να ελένξω αν δουλευει σωστά η εκκρεμής πληρωμή
    #Payment.addNewPayment(parent["Μαρία Παπαδοπούλου"], None, 120.0)
    app = DischargeController(root)
    root.mainloop()
