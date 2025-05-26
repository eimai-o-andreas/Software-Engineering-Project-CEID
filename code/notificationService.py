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