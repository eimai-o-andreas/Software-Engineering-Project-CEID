import tkinter as tk
from parent import Parent
from doctor import Doctor

class Medicine:
    available_medicines = [
        "Παρακεταμόλη",
        "Αμοξικιλλίνη",
        "Ιβουπροφαίνη",
        "Κετοπροφαίνη"
    ]

    @staticmethod
    def getMedicine():
        return Medicine.available_medicines

class PrescriptionController:
    def __init__(self, gui=None, doctor=None, parent=None, medical_record=None):
        self.gui = gui
        self.parent = parent if parent is not None else Parent(1, "Μαρία", "Παπαδοπούλου")
        self.doctor = doctor if doctor is not None else Doctor(2, "Γιώργος", "Ιωαννίδης", "Παιδίατρος")
        self.medical_record = medical_record if medical_record is not None else MedicalRecord(1, self.parent)
        self.medicine_list = []
        

    def getMedicine(self):
        self.medicine_list = Medicine.getMedicine()
        if self.gui:
            self.gui.displayMedicine()
        return self.medicine_list

    def checkDosage(self, medicine, dosage):
        if dosage:
            win = tk.Toplevel(self.gui.root)
            from prescrMed_gui import CreatePrescriptionScreen
            CreatePrescriptionScreen(win, medicine, dosage, self)
        else:
            win = tk.Toplevel(self.gui.root)
            from prescrMed_gui import Message11Screen
            Message11Screen(win)