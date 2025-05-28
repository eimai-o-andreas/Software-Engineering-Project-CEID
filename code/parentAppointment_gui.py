import tkinter as tk
from tkinter import messagebox
from parentAppointment import ParentAppointmentController
from notificationService import NotificationService

class BookAppointmentScreen:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.displayCategoryOptions()

    def displayCategoryOptions(self):
        tk.Label(self.frame, text="Επιλογή Κατηγορίας Θεράποντος", font=("Arial", 14)).pack(pady=10)
        categories = ["Ψυχίατρος", "Μαιευτήρας", "Παιδίατρος"]
        self.category_var = tk.StringVar()
        self.category_var.set(categories[0])

        dropdown = tk.OptionMenu(self.frame, self.category_var, *categories)
        dropdown.pack(pady=5)

        tk.Button(self.frame, text="Επόμενο", command=self.selectCategory).pack(pady=10)

    def selectCategory(self):
        selected_category = self.category_var.get()
        self.controller.sendDoctorCategory(selected_category)

    @staticmethod
    def redirect(window):
        window.destroy()

class AppointmentWaitListScreen:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.displayNoAvailability()
        
    def displayNoAvailability(self):
        tk.Label(self.frame, text="Δεν υπάρχουν διαθέσιμοι γιατροί.").pack(pady=10)
        tk.Button(self.frame, text="Ειδοποίηση Όταν Υπάρξει Διαθεσιμότητα", command=self.enterWaitList).pack()

    def enterWaitList(self):
        self.controller.requestAddToWaitList(category="Ψυχίατρος")

class ChooseDoctorScreen:
    def __init__(self, root, controller, doctors):
        self.root = root
        self.controller = controller
        self.doctors = doctors
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.displayDoctors()

    def displayDoctors(self):
        tk.Label(self.frame, text="Επιλέξτε Θεράποντα").pack(pady=10)
        self.selected_doctor = tk.StringVar(value=self.doctors[0])
        dropdown = tk.OptionMenu(self.frame, self.selected_doctor, *self.doctors)
        dropdown.pack(pady=5)

        tk.Button(self.frame, text="Συνέχεια", command=self.selectDoctor).pack(pady=10)

    def selectDoctor(self):
        self.controller.requestAvailableSlots(self.selected_doctor.get())

class ChooseDatetimeScreen:
    def __init__(self, root, controller, slots):
        self.root = root
        self.controller = controller
        self.slots = slots
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.displayDateTimeOptions()

    def displayDateTimeOptions(self):
        tk.Label(self.frame, text="Επιλογή Ημερομηνίας και Ώρας").pack(pady=10)

        self.selected_slot = tk.StringVar(value=self.slots[0])
        dropdown = tk.OptionMenu(self.frame, self.selected_slot, *self.slots)
        dropdown.pack(pady=5)

        tk.Button(self.frame, text="Αποθήκευση", command=self.confirmSave).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame, text="Άκυρο", command=lambda: BookAppointmentScreen.redirect(self.root)).pack(side=tk.RIGHT, padx=10)

    def confirmSave(self):
        self.controller.createAppointment(self.selected_slot.get())
