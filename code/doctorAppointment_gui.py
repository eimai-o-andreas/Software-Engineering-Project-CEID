from tkinter import *
from tkinter import ttk

class AppointmentRequestScreen(Frame):
    def __init__(self, parent, controller, appointments):
        super().__init__(parent)
        self.controller = controller
        self.appointments = appointments
        self.displayListOfAppointmentRequest(self.appointments)

    def displayListOfAppointmentRequest(self, appointments):
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Patient Name")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=10)

        for app in appointments:
            self.tree.insert("", "end", iid=app["id"], values=(app["id"], app["name"], app["status"]))

        Button(self, text="View Details", command=self.chooseAppointmentReq).pack()

    def chooseAppointmentReq(self):
        selected = self.tree.focus()
        if not selected:
            return
        app_id = int(selected)
        self.controller.fetchAppointmentDetails(app_id)


class AppointmentDetailsScreen(Frame):
    def __init__(self, parent, controller, appointment):
        super().__init__(parent)
        self.controller = controller
        self.appointment = appointment

        Label(self, text=f"ID: {appointment['id']}").pack()
        Label(self, text=f"Patient: {appointment['name']}").pack()
        Label(self, text=f"Status: {appointment['status']}").pack()

        Button(self, text="Accept", command=self.acceptAppointment).pack(pady=5)
        Button(self, text="Reject", command=self.rejectAppointment).pack(pady=5)

    def acceptAppointment(self):
        self.controller.acceptOrRejectAppointment(self.appointment, "accepted")

    def rejectAppointment(self):
        self.controller.acceptOrRejectAppointment(self.appointment, "rejected")


class ConfirmScreen(Frame):
    def __init__(self, parent, controller, status):
        super().__init__(parent)
        self.displayMess(controller, status)

    def displayMess(self, controller, status):
        Label(self, text=f"Appointment {status} successfully!", fg="green", font=("Arial", 14)).pack(pady=20)
        




