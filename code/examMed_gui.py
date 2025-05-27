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
