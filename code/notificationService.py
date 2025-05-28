from tkinter import messagebox
from parent import Parent
from seminars import Seminar

class NotificationService:
    @staticmethod
    def sendMedicationMessageToParent(parent: Parent, medicine, dosage):
        parent.receivePrescription(medicine, dosage)   

    @staticmethod
    def notifyParticipants(seminar: Seminar):
        print(f"Ειδοποίηση: Το σεμινάριο \"{seminar.title}\" ακυρώθηκε.")
    
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
    
    def notifyParentForAppointment(self, patient_name, status):
        print(f"[Notification] Sent to parent of {patient_name} - Appointment status: {status}")
    
    @staticmethod
    def sendSuccessMessage(parent_id):
        print(f"[Ειδοποίηση] Εστάλη ειδοποίηση στον: {parent_id}")

    def notifyParentDischarge(self, parent_id):
        print(f"Γονέας {parent_id}: Το εξιτήριο εκδόθηκε")
    
    def notifyNurse(self, parent_id):
        print(f"Ο ασθενής {parent_id} πήρε εξιτήριο")
    
    def notifyDoctor(self, parent_id):
        print(f"Ο ασθενής {parent_id} πήρε εξιτήριο")


