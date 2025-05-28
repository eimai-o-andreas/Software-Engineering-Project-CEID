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
    def updateRoomAvailability(seminar: Seminar):
        room = seminar.room
        datetime = seminar.datetime
        if room and datetime and room in SeminarRoom.rooms:
            dates = SeminarRoom.rooms[room]
            if datetime in dates:
                dates.remove(datetime)
            if not dates:
                del SeminarRoom.rooms[room]

    @staticmethod
    def getRooms() -> Dict[str, List[str]]:
        return SeminarRoom.rooms

class SeminarCalendar:
    calendar: Dict[str, str] = {}

    @staticmethod
    def getDates(room: str) -> List[str]:
        rooms = SeminarRoom.getRooms()
        return rooms.get(room, [])

    @staticmethod
    def updateCalendar(seminar: Seminar):
        SeminarCalendar.calendar[seminar.title] = seminar.datetime

    @staticmethod
    def makeDateAvailable(seminar: Seminar):
        title = seminar.title
        if title in SeminarCalendar.calendar:
            del SeminarCalendar.calendar[title]

        room = seminar.room
        datetime = seminar.datetime
        if room and datetime:
            rooms = SeminarRoom.getRooms()
            if room in rooms:
                rooms[room].append(datetime)
            else:
                rooms[room] = [datetime]

class SeminarRoomWaitingList:
    waitingList: List[Seminar] = []

    @staticmethod
    def updateWaitList(seminar: Seminar):
        SeminarRoomWaitingList.waitingList.append(seminar)
        print(f"Ειδοποίηση: Το σεμινάριο \"{seminar.title}\" προστέθηκε στη λίστα αναμονής.")


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
    
    def fetchAvailableDates(self, seminar):
        room = seminar.room
        if room:
            return SeminarCalendar.getDates(room)
        else:
            return []

    def fetchSeminarList(self):
        return Seminar.getSeminarList()

  
    def fetchSeminarDetails(self, seminar):
        self.seminar = seminar
        self.clearScreen()
        from seminarsManager_gui import SeminarDetailsScreen
        SeminarDetailsScreen(self.master, self, seminar)


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

  
    def fetchDates(self, seminar):
        self.seminar = seminar
        dates = SeminarCalendar.getDates(seminar.room)
        self.clearScreen()
        from seminarsManager_gui import ViewSeminarCalendarScreen
        ViewSeminarCalendarScreen(self.master, self, seminar, available_dates=dates)


    def saveSeminar(self):
        Seminar.newSeminar(self.seminar)
        SeminarCalendar.updateCalendar(self.seminar)
        SeminarRoom.updateRoomAvailability(self.seminar)
        self.startUI()

 
    def callControllerForDelete(self):
        Seminar.removeSeminar(self.seminar)
        SeminarCalendar.makeDateAvailable(self.seminar)
        NotificationService.notifyParticipants(self.seminar)
        self.startUI()

  
    def callControllerForWaitList(self):
        SeminarRoomWaitingList.updateWaitList(self.seminar)
        from tkinter import messagebox
        messagebox.showinfo("Λίστα Αναμονής", "Το σεμινάριο προστέθηκε στη λίστα αναμονής.")
        self.startUI()
        return "OK"

