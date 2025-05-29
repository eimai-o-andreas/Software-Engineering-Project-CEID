from user import User

class Doctor(User):

    doctors = [
        {"id": "1", "firstname": "Κώστας","lastname": "Αντωνίου", "category": "Μαιευτήρας"},
        {"id": "1", "firstname": "Ελένη","lastname": "Σταυρίδου", "category": "Ψυχίατρος"}
    ]

    def __init__(self, user_id: int, firstname: str, lastname: str, category: str):
        super().__init__(user_id, firstname, lastname)

    @staticmethod
    def getAvailableDoctors(category):
        return [
            f"Δρ. {doc['firstname']} {doc['lastname']}"
            for doc in Doctor.doctors if doc["category"] == category
        ]

    @staticmethod
    def getDoctorList():
        return Doctor.doctors

    @staticmethod
    def removeDoctor(doctor):
        if doctor in Doctor.doctors:
            Doctor.doctors.remove(doctor)
