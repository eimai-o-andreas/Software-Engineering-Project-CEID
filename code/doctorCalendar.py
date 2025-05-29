class DoctorCalendar:

    # Dummy calendar slots
    calendar = {
        "Δρ. Μαρία Παπαδοπούλου": ["2025-06-01 10:00", "2025-06-01 12:00"],
        "Δρ. Κώστας Αντωνίου": ["2025-06-02 09:00"],
        "Δρ. Ελένη Σταυρίδου": ["2025-06-03 14:00"]
    }

    @staticmethod
    def getAvailableSlots(doctor_name):
        return DoctorCalendar.calendar.get(doctor_name, [])

    @staticmethod
    def removeSlot(doctor_name, datetime):
        if doctor_name in DoctorCalendar.calendar:
            if datetime in DoctorCalendar.calendar[doctor_name]:
                DoctorCalendar.calendar[doctor_name].remove(datetime)

    @staticmethod
    def addAppointmentToCalendar(doctor_name, datetime):
        if doctor_name not in DoctorCalendar.calendar:
            DoctorCalendar.calendar[doctor_name] = []
        DoctorCalendar.calendar[doctor_name].append(datetime)

