import tkinter as tk
from user import User
from parent import Parent 
from doctor import Doctor 
from medicalRecord import MedicalRecord 
from notificationService import NotificationService
from exam import Exam
from payment import Payment
from examMed_gui import (
    ExaminationScreen, CreateExaminationScreen, ScheduledExaminationScreen, RejectExaminationScreen
    )

class ExaminationController:
   
    def __init__(self, parent=None, doctor=None):
        self.parent = parent if parent else Parent(1, "Μαρία", "Παπαδοπούλου")
        self.doctor = doctor if doctor else Doctor(2, "Γιώργος", "Ιωαννίδης", "Παιδίατρος")

    def getExams(self):
        return Exam.getExams()
    
    def sendChoosenExams(self, selected_exams):
        already_scheduled = self.handleScheduledExams(selected_exams)
        if already_scheduled:
            win = tk.Toplevel()
            ScheduledExaminationScreen(win, already_scheduled)
        else:
            win = tk.Toplevel()
            CreateExaminationScreen(win, selected_exams, self)