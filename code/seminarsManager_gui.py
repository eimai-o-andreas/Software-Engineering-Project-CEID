import tkinter as tk
from tkinter import messagebox
from seminars import Seminar
from seminarsMan import SeminarRoom, SeminarRoomWaitingList, SeminarCalendar, ManagerSeminarController
from notificationService import NotificationService

class ViewSeminarScreen:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        tk.Label(self.frame, text="Υπάρχοντα Σεμινάρια:", font=("Arial", 14)).pack(pady=10)
        self.displaySeminarList()
        tk.Button(self.frame, text="Προσθήκη Σεμιναρίου", command=self.addNewSeminar).pack(pady=5)

    def displaySeminarList(self):
        # Get seminar list from controller instead of directly from model
        seminars = self.controller.fetchSeminarList()
        
        # Clear any existing seminar display widgets if this method is called multiple times
        for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
                
        # Display seminars
        if not seminars:
            tk.Label(self.frame, text="Δεν υπάρχουν σεμινάρια.", font=("Arial", 10, "italic")).pack(pady=5)
            return
            
        for seminar in seminars:
            frame = tk.Frame(self.frame)
            frame.pack(fill='x', pady=2)
            tk.Label(frame, text=str(seminar)).pack(side='left')
            tk.Button(frame, text="Πληροφορίες", command=lambda s=seminar: self.chooseSeminar(s)).pack(side='right')
    
    def addNewSeminar(self):
        # Hide the current frame and create a new form frame
        self.frame.pack_forget()
        
        # Create a new frame for the seminar form
        self.seminar_form = tk.Frame(self.master)
        self.seminar_form.pack(padx=20, pady=20)
        
        # Add a title for the form
        tk.Label(self.seminar_form, text="Προσθήκη Νέου Σεμιναρίου", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Title field
        tk.Label(self.seminar_form, text="Τίτλος:").grid(row=1, column=0, sticky="w", pady=5)
        self.title_entry = tk.Entry(self.seminar_form, width=40)
        self.title_entry.grid(row=1, column=1, pady=5)
        
        # Description field
        tk.Label(self.seminar_form, text="Περιγραφή:").grid(row=2, column=0, sticky="w", pady=5)
        self.desc_entry = tk.Text(self.seminar_form, width=30, height=4)
        self.desc_entry.grid(row=2, column=1, pady=5)
        
        # Audience field
        tk.Label(self.seminar_form, text="Ακροατήριο:").grid(row=3, column=0, sticky="w", pady=5)
        self.audience_entry = tk.Entry(self.seminar_form, width=40)
        self.audience_entry.grid(row=3, column=1, pady=5)

        tk.Label(self.seminar_form, text="Ομιλητής:").grid(row=4, column=0, sticky="w", pady=5)
        self.speaker_entry = tk.Entry(self.seminar_form, width=40)
        self.speaker_entry.grid(row=4, column=1, pady=5)
        
        # Buttons
        button_frame = tk.Frame(self.seminar_form)
        button_frame.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        tk.Button(button_frame, text="Συνέχεια", command=lambda: self.controller.fetchSeminarRoom(
        self.title_entry.get(),
        self.desc_entry.get("1.0", tk.END).strip(),
        self.audience_entry.get(),
        self.speaker_entry.get()
        )).pack(side=tk.LEFT)
        
    def chooseSeminar(self, seminar):
         # Ask controller to handle getting seminar details
        self.controller.fetchSeminarDetails(seminar)

class ViewSeminarRoomScreen:
    def __init__(self, master, controller, seminar, rooms, edit_mode=False):
        self.master = master
        self.controller = controller
        self.seminar = seminar
        self.rooms = rooms  # <<< πάρθηκε από τον controller
        self.edit_mode = edit_mode

        self.displaySeminarRooms()
        
    def displaySeminarRooms(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Επιλογή Αίθουσας", font=("Arial", 14)).pack(pady=10)

        if not self.rooms:
            tk.Label(self.frame, text="Δεν υπάρχουν διαθέσιμες αίθουσες.").pack()
            return
           
        self.selected_room = tk.StringVar(value=self.seminar.room or self.rooms[0])
        tk.OptionMenu(self.frame, self.selected_room, *self.rooms).pack(pady=5)
        tk.Button(self.frame, text="Καταχώριση", command=self.selectSeminarRoom).pack(pady=10)

    def selectSeminarRoom(self):
        self.seminar.room = self.selected_room.get()
        if self.edit_mode:
            self.controller.clearScreen()
            ViewSeminarCalendarScreen(self.master, self.controller, self.seminar, self.controller.fetchAvailableDates(self.seminar), edit_mode=True)
        else:
            self.controller.fetchDates(self.seminar)

    def redirectToSeminarRoomScreen(controller, master, seminar, rooms):
        controller.clearScreen()
        ViewSeminarRoomScreen(master, controller, seminar, rooms, edit_mode=True)
    

class ViewSeminarCalendarScreen:
    def __init__(self, master, controller, seminar, available_dates, edit_mode=False):
        self.master = master
        self.controller = controller
        self.seminar = seminar
        self.dates = available_dates
        self.edit_mode = edit_mode
    
        self.dates = self.displayDates()
        
    def displayDates(self):
         self.frame = tk.Frame(self.master)
         self.frame.pack()

         tk.Label(self.frame, text="Επιλογή Ημερομηνίας και Ώρας").pack(pady=10)
         self.selected_dt = tk.StringVar(value=self.seminar.datetime or (self.dates[0] if self.dates else ""))
         tk.OptionMenu(self.frame, self.selected_dt, *self.dates).pack()
         tk.Button(self.frame, text="Καταχώριση", command=self.selectDateTime).pack(pady=10)
  
    def selectDateTime(self):
        self.seminar.datetime = self.selected_dt.get()
        if self.edit_mode:
            self.controller.clearScreen()
            ViewSeminarScreen(self.master, self.controller)
        else:
            self.controller.saveSeminar()

    def redirectToSeminarCalendarScreen(master, controller, seminar, edit_mode):
        controller.clearScreen()
        ViewSeminarCalendarScreen(master, controller, seminar, edit_mode)
    
    
class SeminarDetailsScreen:
    def __init__(self, master, controller, seminar):
        self.master = master
        self.controller = controller
        self.seminar = seminar
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.displaySeminarInformation()
    
    def displaySeminarInformation(self):
        tk.Label(self.frame, text=str(self.seminar)).pack(pady=10)
        tk.Button(self.frame, text="Αλλαγή Αίθουσας", command=lambda: ViewSeminarRoomScreen.redirectToSeminarRoomScreen(self.controller, self.master, self.seminar, self.controller.fetchRooms() )).pack()
        tk.Button(self.frame, text="Αλλαγή Ημερομηνίας/Ώρας",
            command=lambda: ViewSeminarCalendarScreen(self.master, self.controller, self.seminar, self.controller.fetchAvailableDates(self.seminar), True)).pack()
        tk.Button(self.frame, text="Διαγραφή Σεμιναρίου", command=self.controller.callControllerForDelete).pack()
    
class Message5Screen:
    def __init__(self, master, controller, seminar):
        self.master = master
        self.controller = controller
        self.seminar = seminar
        self.frame = tk.Frame(master)
        self.frame.pack()

        tk.Label(self.frame, text="Δεν υπάρχει διαθέσιμη αίθουσα.").pack(pady=10)
        tk.Button(self.frame, text="Προσθήκη στη λίστα αναμονής", command=self.addToWaitList).pack()

    def addToWaitList(self):       
        self.controller.callControllerForWaitList()
    
if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("Διαχείριση Σεμιναρίων")
    app = ManagerSeminarController(root)
    root.mainloop()