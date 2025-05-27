from tkinter import messagebox
from seminars import Seminar
from parent import Parent

class NotificationService:  

    @staticmethod
    def notifyParticipants(seminar: Seminar):
        print(f"Ειδοποίηση: Το σεμινάριο \"{seminar.title}\" ακυρώθηκε.")

    @staticmethod
    def sendMedicationMessageToParent(parent: Parent, medicine, dosage):
        parent.receivePrescription(medicine, dosage)   

    @staticmethod       
    def notify(doctor_name):
        messagebox.showinfo("Notification", f"{doctor_name} has been notified")

    @staticmethod
    def sendMessageToParentE(exams):
        print(f"[Notification] Ο γονέας ενημερώθηκε για: {', '.join(exams)}")

    def notifyParent(self, parent_id):
        print(f"Γονέας {parent_id}: Υπάρχουν νέα διαθέσιμα σεμινάρια!")

    def sendMessageToParent(self, appointment):
        message = f"Το ραντεβού με όνομα {appointment['name']} έχει ανατεθεί με επιτυχία."
        messagebox.showinfo("Ειδοποίηση", message)

