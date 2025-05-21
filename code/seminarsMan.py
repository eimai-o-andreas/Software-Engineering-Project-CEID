from typing import List, Dict, Optional
from tkinter import messagebox
from seminars import Seminar
from notificationService import NotificationService

class SeminarRoom:
    rooms: Dict[str, List[str]] = {
        "Αίθουσα 1": ["2025-04-30 10:00", "2025-04-30 12:00"],
        "Αίθουσα 2": ["2025-05-01 09:00", "2025-05-01 11:00"]
    }

    @staticmethod
    def getSeminarsRooms() -> List[str]:
        return list(SeminarRoom.rooms.keys())
    
    @staticmethod
    def getRooms() -> Dict[str, List[str]]:
        return SeminarRoom.rooms

class ManagerSeminarController:
    def __init__(self, master=None):
        self.master = master
        self.seminar = None
        self.startUI()

    def startUI(self):
        self.clearScreen()
        from seminarsManager_gui import ViewSeminarScreen
        ViewSeminarScreen(self.master, self)

    def clearScreen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def fetchRooms(self):
        return SeminarRoom.getSeminarsRooms()
    
    def fetchSeminarList(self):
        return Seminar.getSeminarList()
    
    def fetchSeminarRoom(self, title, desc, audience, speakerName):
        seminar = Seminar(title, desc, audience, speakerName)
        self.seminar = seminar
        rooms = SeminarRoom.getSeminarsRooms()
        self.clearScreen()

        if rooms:
            from seminarsManager_gui import ViewSeminarRoomScreen
            ViewSeminarRoomScreen(self.master, self, seminar, rooms)
        else:
            from seminarsManager_gui import Message5Screen
            Message5Screen(self.master, self, seminar)

  
