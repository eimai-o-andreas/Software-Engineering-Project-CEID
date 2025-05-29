class Appointment:
    appointments = [
        {"id": 1, "name": "Ραντεβού 1", "status": "accepted"},
        {"id": 2, "name": "Ραντεβού 2", "status": "accepted"},
        {"id": 3, "name": "Ραντεβού 3", "status": "accepted"}
    ]

    def __init__(self, doctor, patient_name, room, datetime_start, datetime_end):
        self.doctor = doctor
        self.patient_name = patient_name
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.room = room

    @classmethod
    def addAppointment(cls, appointment):
        cls.appointments.append(appointment)

    @classmethod
    def getAppointment(cls):
        return cls.appointments

    @classmethod
    def getAppointmentDetails(cls, app_id):
        return next((a for a in cls.getAppointment() if a["id"] == app_id), None)

    @classmethod
    def updateAppointment(cls, appointment, room, nurses):
        for app in cls.appointments:
            if app["id"] == appointment["id"]:
                app["status"] = "assigned"
                app["room"] = room
                app["nurses"] = nurses
