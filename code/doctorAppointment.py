from tkinter import *
from appointment import Appointment
from notificationService import NotificationService
from doctorAppointment_gui import AppointmentRequestScreen, AppointmentDetailsScreen, ConfirmScreen

class AppointmentController:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Appointment Management")

        self.notifier = NotificationService()
        self.current_screen = None

        appointments = Appointment.getAppointment()
        screen = AppointmentRequestScreen(self.root, self, appointments)

        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = screen
        self.current_screen.pack(fill="both", expand=True)

    def fetchAppointmentDetails(self, app_id):
        appointment = Appointment.getAppointmentDetails(app_id)
        if appointment:
            screen = AppointmentDetailsScreen(self.root, self, appointment)
            if self.current_screen:
                self.current_screen.destroy()
            self.current_screen = screen
            self.current_screen.pack(fill="both", expand=True)

    def acceptOrRejectAppointment(self, appointment, new_status):
        Appointment.updateAppointment(appointment, room=None, nurses=None)
        appointment["status"] = new_status

        self.notifier.notifyParentForAppointment(appointment["name"], new_status)
        screen = ConfirmScreen(self.root, self, new_status)
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = screen
        self.current_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = Tk()
    app = AppointmentController(root)
    root.mainloop()

