from tkinter import messagebox
from appointment import Appointment
from doctor import Doctor
from doctorCalendar import DoctorCalendar
from notificationService import NotificationService

class AppointmentWaitList:
    waiting_list = []

    @staticmethod
    def addToWaitList(appointment):
        AppointmentWaitList.waiting_list.append(appointment)

class ParentAppointmentController:
    def __init__(self, master):
        self.master = master
        self.startUI()

    def startUI(self):
            self.clearScreen()
            from parentAppointment_gui import BookAppointmentScreen
            BookAppointmentScreen(self.master, self)

    def sendDoctorCategory(self, category):
        doctors = Doctor.getAvailableDoctors(category)
        self.clearScreen()
        if not doctors:
            from parentAppointment_gui import AppointmentWaitListScreen
            AppointmentWaitListScreen(self.master, self)
        else:
            from parentAppointment_gui import ChooseDoctorScreen
            ChooseDoctorScreen(self.master, self, doctors)

    def requestAddToWaitList(self, category=None):
        from appointment import Appointment
        from datetime import datetime

        dummy_datetime = datetime.now()

        appointment = Appointment(
            doctor=None,                           
            patient_name="Μαρία Παπαδοπούλου",
            room = None,
            datetime_start=dummy_datetime,
            datetime_end=dummy_datetime
        )
        AppointmentWaitList.addToWaitList(appointment)
        messagebox.showinfo("Λίστα Αναμονής", "Προστέθηκε στη λίστα αναμονής.")


    def requestAvailableSlots(self, doctor_name):
        self.selected_doctor = doctor_name
        slots = DoctorCalendar.getAvailableSlots(doctor_name)
        self.clearScreen()
        from parentAppointment_gui import ChooseDatetimeScreen
        ChooseDatetimeScreen(self.master, self, slots)

    def createAppointment(self, datetime):
        # Δημιουργία ραντεβού
        appointment = Appointment(self.selected_doctor, "Μαρία Παπαδοπούλου", "Room A", datetime, datetime)
        Appointment.addAppointment(appointment)
        # Ειδοποίηση γιατρού
        NotificationService.notify(self.selected_doctor)
        # Αφαίρεση slot από calendar
        DoctorCalendar.removeSlot(self.selected_doctor, datetime)
        messagebox.showinfo("Επιτυχία", "Το ραντεβού καταχωρήθηκε με επιτυχία.")
        self.startUI()

        
    def clearScreen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

# Εκκίνηση εφαρμογής
if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("Ραντεβού")
    app = ParentAppointmentController(root)
    root.mainloop()