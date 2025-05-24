from typing import List, Optional
from datetime import datetime

class Seminar:
    seminars: List['Seminar'] = []
    _next_id: int = 1

    def __init__(self, title: str, description: str, audience: str, speakerName: str, room: Optional[str] = None, datetime: Optional[str] = None):
        self.id = Seminar._next_id
        Seminar._next_id += 1

        self.title = title
        self.description = description
        self.audience = audience
        self.speakerName = speakerName
        self.room = room
        self.datetime = datetime
        self.participants_manager = 2
        self.is_full = False

    @staticmethod
    def getSeminarList() -> List['Seminar']:
        return Seminar.seminars

    @staticmethod
    def newSeminar(seminar: 'Seminar'):
        Seminar.seminars.append(seminar)

    @staticmethod
    def removeSeminar(seminar: 'Seminar'):
        if seminar in Seminar.seminars:
            Seminar.seminars.remove(seminar)

 
    