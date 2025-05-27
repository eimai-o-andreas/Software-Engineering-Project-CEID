import tkinter as tk
from tkinter import messagebox
from parent import Parent

class SearchParentScreen:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.displaySearch()

    def displaySearch(self):
        self.root.title("Αναζήτηση Γονέα")

        tk.Label(self.root, text="Όνομα:").pack(pady=5)
        self.firstname_entry = tk.Entry(self.root, width=40)
        self.firstname_entry.pack()

        tk.Label(self.root, text="Επίθετο:").pack(pady=5)
        self.lastname_entry = tk.Entry(self.root, width=40)
        self.lastname_entry.pack()

        tk.Button(self.root, text="Αναζήτηση", command=self.giveParentName).pack(pady=5)

    def giveParentName(self):
        firstname = self.firstname_entry.get().strip()
        lastname = self.lastname_entry.get().strip()
        success = self.controller.fetchMedicalRecord(firstname, lastname)

        if success:
            self.root.destroy()
        else:
            messagebox.showerror("Σφάλμα", "Ο γονέας δεν βρέθηκε.")

class MedicalRecordScreen:
    def __init__(self, root, parent_obj, controller):
        self.root = root
        self.parent = parent_obj
        self.controller = controller
        self.displayMedicalRecord()

    def displayMedicalRecord(self):
        self.root.title(f"Ιατρικός Φάκελος - {self.parent.firstname} {self.parent.lastname}")

        record_data = self.controller.record.getData()
        notes = record_data["notes"]

        tk.Label(self.root, text=f"Ιατρικός Φάκελος για: {self.parent.firstname} {self.parent.lastname}",
                 font=("Arial", 12, "bold")).pack()

        self.text_area = tk.Text(self.root, width=60, height=10)
        current_data = "\n".join([note for note, _ in notes])
        self.text_area.insert(tk.END, current_data)
        self.text_area.pack(pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Προσθήκη Σημείωσης", command=self.addNewNote).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Συνταγογράφηση", command=self.addNewPrescription).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Ανάθεση Εξετάσεων", command=self.addNewExamination).grid(row=0, column=2, padx=5)

    def addNewNote(self):
        new_note = self.text_area.get("1.0", tk.END).strip()
        if not new_note:
            tk.messagebox.showwarning("Προσοχή", "Η σημείωση είναι κενή.")
            return
        self.controller.requestConfirmation(self.root, new_note)

    def addNewPrescription(self):
        new_window = tk.Toplevel(self.root)
        from presMed import PrescriptionController
        controller = PrescriptionController()
        controller.showMedicineScreen(new_window, self.parent)

    def addNewExamination(self):
        new_window = tk.Toplevel(self.root)
        from examMed import ExaminationController
        controller = ExaminationController(parent=self.parent)
        controller.showExaminationScreen(new_window)

    @staticmethod
    def redirectToMedicalRecordScreen(window):
        window.destroy()

class NoteConfirmationScreen:
    def __init__(self, parent_window, parent_obj, note, controller):
        self.parent_window = parent_window
        self.parent = parent_obj
        self.note = note
        self.controller = controller
        self.displayConfirmation()

    def displayConfirmation(self):
        self.top = tk.Toplevel(self.parent_window)
        self.top.title("Επιβεβαίωση")

        tk.Label(self.top, text="Επιβεβαιώνετε την αποθήκευση της σημείωσης;").pack(padx=20, pady=10)

        button_frame = tk.Frame(self.top)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Ναι", command=self.confirm).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Όχι", command=lambda: MedicalRecordScreen.redirectToMedicalRecordScreen(self.top)).pack(side=tk.LEFT, padx=10)

    def confirm(self):
        self.controller.saveNote(self.parent, self.note)
        self.top.destroy()


if __name__ == "__main__":
    from medRecord import MedicalRecordController
    root = tk.Tk()
    root.withdraw()
    controller = MedicalRecordController(gui=root)
    app = SearchParentScreen(tk.Toplevel(root), controller)
    root.mainloop()
