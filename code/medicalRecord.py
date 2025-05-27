from parent import Parent
from doctor import Doctor

class MedicalRecord:
    medical_records = {}
    
    def __init__(self, medical_record_id: int, parent: Parent):
        self.id = medical_record_id
        self.parent = parent
        self.medications = []  # List of tuples: (medicine, dosage)
        self.notes = []  # List of tuples: (note, doctor)

     # Καταχώρηση του φακέλου με βάση το πλήρες όνομα του γονέα
        MedicalRecord.medical_records[f"{parent.firstname} {parent.lastname}"] = self

    def updateMedicalRecordM(self, medicine, dosage):
        self.medications.append((medicine, dosage))
        print(f"Medical record updated: {medicine} - {dosage}")

    def updateMedicalRecord(self, note, parent: Parent, doctor: Doctor):
        self.notes.append((note, doctor))
        print(f"Medical record updated by {doctor.firstname} {doctor.lastname}, note: {note}")

    def getData(self):
        return {
            "notes": self.notes,
            "medications": self.medications
        }

    @staticmethod
    def getMedicalRecord(full_name: str):
        return MedicalRecord.medical_records.get(full_name)

parent = {
    "Μαρία Παπαδοπούλου": Parent(1, "Μαρία", "Παπαδοπούλου"),
    "Ελένη Παππά": Parent(2, "Ελένη", "Παππά")
}

medical_records = {
    "Μαρία Παπαδοπούλου": MedicalRecord(1, parent["Μαρία Παπαδοπούλου"]),
    "Ελένη Παππά": MedicalRecord(2, parent["Ελένη Παππά"])
}