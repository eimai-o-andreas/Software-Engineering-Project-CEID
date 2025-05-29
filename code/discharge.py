
class Discharge:
    discharges = []

    def __init__(self, parent_id, doctor_id, nurses, room_id):
        self.parent_id = parent_id
        self.doctor_id = doctor_id
        self.nurses = nurses
        self.room_id = room_id

    @staticmethod
    def createDischarge(discharge):
        Discharge.discharges.append(discharge)