

class Doctor(User):

    doctors = [
        {"id": "1", "firstname": "Κώστας","lastname": "Αντωνίου", "category": "Μαιευτήρας"},
        {"id": "1", "firstname": "Ελένη","lastname": "Σταυρίδου", "category": "Ψυχίατρος"}
    ]

    def __init__(self, user_id: int, firstname: str, lastname: str, category: str):
        super().__init__(user_id, firstname, lastname)
