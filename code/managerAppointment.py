# controller_and_services.py
from tkinter import messagebox
from nurse import Nurse
from notificationService import NotificationService
from appointment import Appointment
from typing import List, Dict, Optional
from room import Room

class ManageAppointmentController:
    def __init__(self, root, appointment_service, room_service, nurse_service, notification_service):
        self.root = root
        self.appointment_service = appointment_service
        self.room_service = room_service
        self.nurse_service = nurse_service
        self.notification_service = notification_service

        self.selected_appointment = None
        self.selected_room = None
        self.selected_nurses = []

    def start(self):
        from managerAppointment_gui import ViewAppointmentScreen
        ViewAppointmentScreen(self.root, self)

    def fetchAppointments(self):
        all_appointments = self.appointment_service.getAppointment()
        filtered = [app for app in all_appointments if app["status"] == "accepted"]
        return filtered

    def fetchAvailableRooms(self):
        rooms = self.room_service.getAvailableRooms()
        if rooms:
            from managerAppointment_gui import RoomScreen
            RoomScreen(self.root, self, rooms)
        else:
            from managerAppointment_gui import AssignmentWaitingListScreen
            AssignmentWaitingListScreen(self.root, self)

    def fetchAvailableNurses(self, room):
        self.selected_room = room
        self.room_service.assignRooms(room)
        self.room_service.updateRooms(room)
        nurses = self.nurse_service.getAvailableNurses()
        if nurses:
            from managerAppointment_gui import ViewNurseScreen
            ViewNurseScreen(self.root, self, nurses)
        else:
            from managerAppointment_gui import NurseNotificationScreen
            NurseNotificationScreen(self.root, self)

    def requestConfirmation(self, nurses):
        self.selected_nurses = nurses
        from managerAppointment_gui import ConfirmAssignmentScreen
        ConfirmAssignmentScreen(self.root, self, self.selected_appointment, self.selected_room, self.selected_nurses)

    def callControllerForSave(self):
            self.appointment_service.updateAppointment(self.selected_appointment, self.selected_room, self.selected_nurses)
            self.nurse_service.assignNurses(self.selected_nurses)
            self.notification_service.sendMessageToParent(self.selected_appointment)
            messagebox.showinfo("Επιτυχία", "Η ανάθεση ολοκληρώθηκε!")
    
    def callControllerForReject(self):
        self.room_service.updateRoomAsAvailable(self.selected_room)
 
    def notifyParentNoNurses(self):
        message = f"Όταν υπάρξουν διαθέσιμοι νοσηλευτές θα υπάρξει ενημέρωση"
        messagebox.showinfo("Ειδοποίηση", message)
        self.notification_service.sendMessageToParent(self.selected_appointment)
        self.start()

    def callWaitingListService(self):
        RoomWaitList.updateWaitList(self.selected_appointment["id"])
        print("Προστέθηκε στη λίστα αναμονής.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

class RoomWaitList:
    waitingList: List[Appointment] = []

    @staticmethod
    def updateWaitList(appointment: Appointment):
        RoomWaitList.waitingList.append(appointment)
        print(f"Ειδοποίηση: Το Ραντεβού προστέθηκε στην λίστα αναμονής για δωμάτιο \"{appointment}\" .")
