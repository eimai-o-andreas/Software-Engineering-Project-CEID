from user import User

class Nurse(User):
    def __init__(self, user_id: int, firstname: str, lastname: str):
        super().__init__(user_id, firstname, lastname)
        self.nurses = ["Νοσηλευτής 1", "Νοσηλευτής 2", "Νοσηλευτής 3"]

    def getAvailableNurses(self):
        return self.nurses

    def assignNurses(self, selected):
        for n in selected:
            if n in self.nurses:
                self.nurses.remove(n)

    def updateAvailableNurses(self, nurses):
        for n in nurses:
            if n not in self.nurses:
                self.nurses.append(n)
                print(f"Οι Νοσηλευτές ενημερώθηκαν")