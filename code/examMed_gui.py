import tkinter as tk
from tkinter import messagebox

class ExaminationScreen:
    def __init__(self, root, controller, parent_name="Γονέας"):
        self.root = root
        self.parent_name = parent_name
        self.controller = controller
        self.all_exams = self.controller.getExams()
        self.exam_vars = {}
        self.displayExams()

    def displayExams(self):
        self.root.title("Επιλογή Εξετάσεων")

        tk.Label(self.root, text="Επιλογή Εξετάσεων:").pack(pady=5)
        tk.Label(self.root, text=f"Για: {self.parent_name}", font=("Arial", 12, "bold")).pack(pady=5)

        for exam in self.all_exams:
            var = tk.IntVar()
            self.exam_vars[exam] = var
            tk.Checkbutton(self.root, text=f"{exam} ({self.all_exams[exam]}€)", variable=var).pack(anchor="w")

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Έλεγχος", command=self.chooseExams).grid(row=0, column=0, padx=5)

    def chooseExams(self):
        selected_exams = [exam for exam, var in self.exam_vars.items() if var.get() == 1]

        if not selected_exams:
            messagebox.showerror("Αποτυχία", "Δεν επιλέχθηκαν εξετάσεις.")
            return
        self.controller.sendChoosenExams(selected_exams)

    @staticmethod
    def redirectToExaminationScreen(root):
        root.destroy()


class CreateExaminationScreen:
    def __init__(self, root, selected_exams, controller):
        self.root = root
        self.controller = controller
        self.selected_exams = selected_exams
        self.displayCreateExaminationScreen()

    def displayCreateExaminationScreen(self):
        self.root.title("Επιτυχής Επιλογή Εξετάσεων")

        tk.Label(self.root, text="Θέλετε να αποθηκεύσετε τις εξετάσεις;").pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Αποθήκευση", command=self.acceptExams).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Ακύρωση", command=self.rejectExams).grid(row=0, column=1, padx=5)

    def acceptExams(self):
        self.controller.acceptOrReject(self.selected_exams, True)
        self.root.destroy()

    def rejectExams(self):
        self.controller.acceptOrReject(self.selected_exams, False)
        self.root.destroy()


class ScheduledExaminationScreen:
    def __init__(self, root, already_scheduled):
        self.root = root
        self.already_scheduled = already_scheduled
        self.displayScheduledExaminationsMessage()

    def displayScheduledExaminationsMessage(self):
        self.root.title("Προγραμματισμένες Εξετάσεις")

        tk.Label(self.root, text="Οι παρακάτω εξετάσεις είναι ήδη προγραμματισμένες:").pack(pady=5)

        for exam in self.already_scheduled:
            tk.Label(self.root, text=exam).pack(anchor="w")

        tk.Button(self.root, text="Επιστροφή", command=lambda: ExaminationScreen.redirectToExaminationScreen(self.root)).pack(pady=10)


class RejectExaminationScreen:
    def __init__(self, root):
        self.root = root
        self.displayRejectScreen()

    def displayRejectScreen(self):
        self.root.title("Απόρριψη Εξέτασης")
        tk.Label(self.root, text="Θέλετε να απορριψετε;.").pack(pady=10)
        tk.Button(self.root, text="Επιβεβαίωση", command=self.root.destroy).pack(pady=10)


    if __name__ == "__main__":
     import examMed  
     root = tk.Tk()
     controller = examMed.ExaminationController()
     parent = "Γονέας"
     app = ExaminationScreen(root, controller, parent)
     
     root.mainloop()
