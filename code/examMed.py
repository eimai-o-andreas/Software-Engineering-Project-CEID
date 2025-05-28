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


class Examination:
    next_id = 1
    all_examinations = []

    def __init__(self, parent, doctor, exams):
        self.id = Examination.next_id
        Examination.next_id += 1

        self.parent = parent
        self.doctor = doctor
        self.scheduled_exams = set(exams)

        Examination.all_examinations.append(self)

    @staticmethod
    def addNewExamination(parent, doctor, exams):
        print(f"[Examination] Νέες εξετάσεις προστέθηκαν: {exams}")
        return Examination(parent, doctor, exams)

    @staticmethod
    def checkScheduledExams(chosen_exams):
        scheduled = set()
        for exam_obj in Examination.all_examinations:
            scheduled.update(exam_obj.scheduled_exams)
        return [exam for exam in chosen_exams if exam in scheduled]


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

    def handleScheduledExams(self, exams):
        return Examination.checkScheduledExams(exams)
    
    def calculateCost(self, exams):
        return sum(Exam.available_exams.get(exam, 0) for exam in exams)
         
    def acceptOrReject(self, exams, save):
        if save:
            exam = Examination.addNewExamination(self.parent, self.doctor, exams)
            NotificationService.sendMessageToParentE(exams)
            cost = self.calculateCost(exams)
            Payment.addNewPayment(self.parent, exam, cost)
            return cost
        else:
            win = tk.Toplevel()
            RejectExaminationScreen(win)

