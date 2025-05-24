

class Parent(User):
    all_parents = {}

    def __init__(self, user_id: int, firstname: str, lastname: str):
        super().__init__(user_id, firstname, lastname)

        self.id = user_id
        self.firstname = firstname
        self.lastname = lastname

    def receivePrescription(self, medicine, dosage):
        print(f"Ο γονέας {self.firstname} ενημερώθηκε: Συνταγή για {medicine} - {dosage}")

    @staticmethod
    def getParent(firstname, lastname):
        full_name = f"{firstname} {lastname}"
        return parent.get(full_name)
    
parent = {
    "Μαρία Παπαδοπούλου": Parent(1, "Μαρία", "Παπαδοπούλου"),
    "Ελένη Παππά": Parent(2, "Ελένη", "Παππα")
}