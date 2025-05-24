from tkinter import messagebox
from seminars import Seminar

class NotificationService:  

    @staticmethod
    def notifyParticipants(seminar: Seminar):
        print(f"Ειδοποίηση: Το σεμινάριο \"{seminar.title}\" ακυρώθηκε.")