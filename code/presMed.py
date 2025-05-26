import tkinter as tk
from parent import Parent
from doctor import Doctor
from medicalRecord import MedicalRecord 
from notificationService import NotificationService

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
    
class Prescription:
    _next_id = 1
    prescriptions = []

    def __init__(self, medicine, dosage, parent: Parent, doctor: Doctor, medical_record: MedicalRecord):
        self.id = Prescription._next_id
        Prescription._next_id += 1

        self.medicine = medicine
        self.dosage = dosage
        self.parent = parent
        self.doctor = doctor
        self.medical_record = medical_record

        Prescription.prescriptions.append(self)

    @staticmethod
    def addNewPrescription(medicine, dosage, parent: Parent, doctor: Doctor, medical_record: MedicalRecord):
        return Prescription(medicine, dosage, parent, doctor, medical_record)

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

    def acceptOrRejectPrescription(self, medicine_name, dosage, save):
        if save:
            Prescription.addNewPrescription(
                medicine_name,
                dosage,
                self.parent,
                self.doctor,
                self.medical_record
            )
            self.medical_record.updateMedicalRecordM(medicine_name, dosage)
            NotificationService.sendMedicationMessageToParent(self.parent, medicine_name, dosage)
            print(f"Η συνταγή για {medicine_name} με δοσολογία {dosage} αποθηκεύτηκε.")
        else:
            win = tk.Toplevel(self.gui.root)
            from prescrMed_gui import RejectPrescriptionScreen
            RejectPrescriptionScreen(win)
