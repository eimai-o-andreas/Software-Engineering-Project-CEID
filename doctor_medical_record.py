import tkinter as tk
from tkinter import messagebox

class PrescriptionSystem:
    def __init__(self, root, parent_name):
        self.root = root
        self.root.title("Συνταγογράφηση Φαρμάκων")
        self.parent_name = parent_name
        self.medicines = ["Παρακεταμόλη", "Αντιβίωση", "Ιβουπροφαίνη", "Σιρόπι Βήχα"]

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text=f"Συνταγογράφηση για: {self.parent_name}", font=("Arial", 12, "bold")).pack(pady=5)

        tk.Label(self.root, text="Επιλέξτε Φάρμακο:").pack()
        self.selected_medicine = tk.StringVar()
        self.selected_medicine.set(self.medicines[0])
        tk.OptionMenu(self.root, self.selected_medicine, *self.medicines).pack()

        tk.Label(self.root, text="Δοσολογία:").pack(pady=(10, 0))
        self.dosage_entry = tk.Entry(self.root, width=40)
        self.dosage_entry.pack()

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Αποθήκευση Συνταγής", command=self.save_prescription).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Ακύρωση", command=self.cancel_prescription).grid(row=0, column=1, padx=5)

    def save_prescription(self):
        medicine = self.selected_medicine.get()
        dosage = self.dosage_entry.get().strip()

        if not dosage:
            messagebox.showerror("Σφάλμα", "Η δοσολογία είναι υποχρεωτική.")
            return

        messagebox.showinfo("Επιτυχία", f"Η συνταγή για {medicine} αποθηκεύτηκε με δοσολογία: {dosage}.\nΕνημερώθηκε ο ιατρικός φάκελος και στάλθηκε ειδοποίηση.")
        self.root.destroy()

    def cancel_prescription(self):
        if messagebox.askyesno("Επιβεβαίωση", "Είστε σίγουροι ότι θέλετε να ακυρώσετε τη συνταγή;"):
            messagebox.showinfo("Ακύρωση", "Η συνταγή ακυρώθηκε.")
            self.root.destroy()


class ExaminationSystem:
    def __init__(self, root, parent_name):
        self.root = root
        self.parent_name = parent_name
        self.root.title("Διεξαγωγή Εξετάσεων")
        self.exams = ["Αιματολογική", "Υπέρηχος", "Ουρολογική", "Μαγνητική"]
        self.scheduled_exams = {"Αιματολογική"}

        self.selected_exams = []
        self.render_exam_ui()

    def render_exam_ui(self):
        tk.Label(self.root, text=f"Ανάθεση Εξετάσεων για: {self.parent_name}", font=("Arial", 12, "bold")).pack(pady=5)

        self.exam_vars = {}
        for exam in self.exams:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.root, text=exam, variable=var)
            cb.pack(anchor='w')
            self.exam_vars[exam] = var

        tk.Button(self.root, text="Αποθήκευση", command=self.save_exams).pack(pady=10)

    def save_exams(self):
        chosen = [exam for exam, var in self.exam_vars.items() if var.get()]
        already_scheduled = set(chosen) & self.scheduled_exams

        if already_scheduled:
            msg = "Ήδη προγραμματισμένες εξετάσεις:\n" + ", ".join(already_scheduled)
            messagebox.showwarning("Προγραμματισμένες", msg)
            return

        if not chosen:
            messagebox.showerror("Σφάλμα", "Δεν επιλέχθηκαν εξετάσεις.")
            return

        cost = len(chosen) * 30
        messagebox.showinfo("Επιτυχία", f"Αποθηκεύτηκαν {len(chosen)} εξετάσεις.\nΚόστος: {cost}€")
        self.root.destroy()


class MedicalRecordSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Ενημέρωση Ιατρικού Φακέλου - Μαιευτήριο")

        self.parents = {
            "Μαρία Παπαδοπούλου": "Μαιευτήριο - Φάκελος: Είσοδος στις 20/04\nΤοκετός 21/04 - Καισαρική.",
            "Γιώργος Κωνσταντίνου": "Μαιευτήριο - Φάκελος: Σύζυγος σε παρακολούθηση εγκυμοσύνης.",
        }

        self.create_search_ui()

    def create_search_ui(self):
        tk.Label(self.root, text="Αναζήτηση Γονέα:").pack(pady=5)
        self.search_entry = tk.Entry(self.root, width=40)
        self.search_entry.pack()
        tk.Button(self.root, text="Αναζήτηση", command=self.search_parent).pack(pady=5)

        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=10)

    def search_parent(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        name = self.search_entry.get().strip()
        if name in self.parents:
            tk.Label(self.result_frame, text=f"Ιατρικός Φάκελος για: {name}", font=("Arial", 12, "bold")).pack()

            self.text_area = tk.Text(self.result_frame, width=60, height=10)
            self.text_area.insert(tk.END, self.parents[name])
            self.text_area.pack(pady=5)

            btn_frame = tk.Frame(self.result_frame)
            btn_frame.pack()

            tk.Button(btn_frame, text="Προσθήκη Σημείωσης", command=self.confirm_save).grid(row=0, column=0, padx=5)
            tk.Button(btn_frame, text="Συνταγογράφηση", command=self.prescribe).grid(row=0, column=1, padx=5)
            tk.Button(btn_frame, text="Ανάθεση Εξετάσεων", command=self.order_exams).grid(row=0, column=2, padx=5)

            self.current_parent = name
        else:
            messagebox.showerror("Σφάλμα", "Ο γονέας δεν βρέθηκε.")

    def confirm_save(self):
        new_note = self.text_area.get("1.0", tk.END).strip()
        if not new_note:
            messagebox.showwarning("Άδεια Σημείωση", "Δεν πληκτρολογήσατε καμία σημείωση.")
            return

        response = messagebox.askyesno("Επιβεβαίωση", "Θέλετε να προσθέσετε αυτή τη σημείωση στον φάκελο;")
        if response:
            old_notes = self.parents[self.current_parent]
            combined = old_notes + "\n\nΣημείωση: " + new_note
            self.parents[self.current_parent] = combined
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, combined)
            messagebox.showinfo("Επιτυχία", "Η σημείωση προστέθηκε στον ιατρικό φάκελο.")
        else:
            messagebox.showinfo("Ακύρωση", "Η σημείωση δεν αποθηκεύτηκε.")

    def prescribe(self):
        new_window = tk.Toplevel(self.root)
        PrescriptionSystem(new_window, self.current_parent)

    def order_exams(self):
        new_window = tk.Toplevel(self.root)
        ExaminationSystem(new_window, self.current_parent)

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalRecordSystem(root)
    root.mainloop()

