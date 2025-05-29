import tkinter as tk
from tkinter import messagebox

class ViewSeminarScreen:
    def __init__(self, controller, master, seminars):
        self.controller = controller  
        self.master = master
        self.seminars = seminars
        self.displayListOfSeminars()

    def displayListOfSeminars(self):
        self.controller.clear()  
        tk.Label(self.master, text="Λίστα Σεμιναρίων:").pack()
        self.listbox = tk.Listbox(self.master, width=60, height=6)
        for s in self.seminars:
            self.listbox.insert(tk.END, f"{s.title} - {s.datetime}")
        self.listbox.pack()
        tk.Button(self.master, text="Επιλογή", command=self.selectSeminar).pack()
        tk.Button(self.master, text="Θέλω να ενημερωθώ", command=self.selectToBeNotified).pack()

    def selectSeminar(self):
        try:
            idx = self.listbox.curselection()[0]
            seminar = self.seminars[idx]
            self.controller.fetchSeminarDetails(seminar)
        except IndexError:
            messagebox.showwarning("Προσοχή", "Επιλέξτε ένα σεμινάριο.")

    def selectToBeNotified(self):
        self.controller.checkForNewSeminars()

    @staticmethod
    def redirect(controller, master):
        seminars = controller.start()

class ViewSeminarDetailsScreen:
    def __init__(self, controller, master, seminar):
        self.controller = controller
        self.master = master
        self.seminar = seminar
        self.displaySeminarDetails()

    def displaySeminarDetails(self):
        self.controller.clear()
        tk.Label(self.master, text=f"Τίτλος: {self.seminar.title}").pack()
        tk.Label(self.master, text=f"Ημερομηνία: {self.seminar.datetime}").pack()
        tk.Label(self.master, text=f"Περιγραφή: {self.seminar.description}").pack()
        tk.Label(self.master, text=f"Απευθύνεται σε: {self.seminar.audience}").pack()
        tk.Label(self.master, text=f"Αίθουσα: {self.seminar.room}").pack()
        tk.Button(self.master, text="Δήλωση Συμμετοχής", command=self.chooseToParticipate).pack()

    def chooseToParticipate(self):
        self.controller.checkAvailability()


class Confirm3Screen:
    def __init__(self, controller, master, seminar):
        self.controller = controller
        self.master = master
        self.seminar = seminar
        self.showConfirmationScreen()

    def showConfirmationScreen(self):
        self.controller.clear()
        tk.Label(self.master, text="Επιβεβαιώνετε τη συμμετοχή σας;").pack()
        tk.Button(self.master, text="Ναι", command=self.confirmParticipation).pack()
        tk.Button(self.master, text="Όχι", command=self.rejectParticipation).pack()

    def confirmParticipation(self):
        self.controller.actOnParticipation()

    def rejectParticipation(self):
        ViewSeminarScreen.redirect(self.controller, self.master)

class FMessage3Screen:
    def __init__(self, controller, master):
        self.controller = controller
        self.master = master
        self.displayNoSeminarsFound()

    def displayNoSeminarsFound(self):
        self.controller.clear()
        tk.Label(self.master, text="Δεν υπάρχουν διαθέσιμα σεμινάρια.").pack()
        tk.Button(self.master, text="Ενημέρωσέ με όταν υπάρξουν", command=self.chooseNotification).pack()

    def chooseNotification(self):
        self.controller.addToNotificationWaitList()

    