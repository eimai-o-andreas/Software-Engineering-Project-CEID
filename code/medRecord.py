import tkinter as tk
from parent import Parent
from medicalRecord import MedicalRecord
from doctor import Doctor

class MedicalRecordController:
    def __init__(self, gui=None, doctor=None):
        self.parent = None
        self.record = None
        self.doctor = doctor if doctor else Doctor(2, "Γιώργος", "Ιωαννίδης", "Γενικός")
        self.gui = gui

    def fetchMedicalRecord(self, firstname, lastname):
        full_name = f"{firstname} {lastname}"
        parent_obj = Parent.getParent(firstname, lastname)

        if parent_obj:
            self.parent = parent_obj
            self.record = MedicalRecord.getMedicalRecord(full_name)

            if self.record:
                from medicalRecord_gui import MedicalRecordScreen
                win = tk.Toplevel(self.gui)  # Δημιουργία παραθύρου για το MedicalRecordScreen
                MedicalRecordScreen(win, self.parent, self)
                return True

        return False

    def saveNote(self, parent_obj, note):
        if self.record:
            self.record.updateMedicalRecord(note, parent_obj, self.doctor)
        
    def requestConfirmation(self, parent_window, note):
        from medicalRecord_gui import NoteConfirmationScreen
        NoteConfirmationScreen(parent_window, self.parent, note, self)
