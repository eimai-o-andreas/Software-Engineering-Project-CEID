class Room:
    def __init__(self):
        self.rooms = ["Δωμάτιο 1", "Δωμάτιο 2", "Δωμάτιο 3"]

    def getAvailableRooms(self):
        return self.rooms

    def assignRooms(self, room):
        print(f"Room has been assigned")
    
    def updateRooms(self, room):
        if room in self.rooms:
            self.rooms.remove(room)
        
    def updateRoomAsAvailable(self, room):
        if room not in self.rooms:
            self.rooms.append(room)
