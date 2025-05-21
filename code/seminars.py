from seminarParticipants import SeminarParticipants
from datetime import datetime

class Seminar:
    seminars = []

    def __init__(self, title, description, audience, room=None, datetime=None):
        self.title = title
        self.description = description
        self.audience = audience
        self.room = room
        self.datetime = datetime
        self.participants_manager = SeminarParticipants(capacity=5)
        self.is_full = False

    @staticmethod
    def getSeminarList():
        Seminar.load_dummy_data()
        return Seminar.seminars
