import tkinter as tk

class MedicineScreen:
    def __init__(self, root, controller, parent):
        self.root = root
        self.controller = controller
        self.parent = parent
        self.controller.getMedicine() 

    def displayMedicine(self):
        self.root.title("Επιλογή Φαρμάκου")
        self.all_medicine = list(self.controller.medicine_list)
        self.selected_medicine = tk.StringVar(value=self.all_medicine[0] if self.all_medicine else "")
        
        tk.Label(self.root, text="Επιλογή Φαρμάκου:").pack(pady=5)
        tk.OptionMenu(self.root, self.selected_medicine, *self.all_medicine).pack()
        
        tk.Label(self.root, text="Δοσολογία:").pack(pady=5)
        self.dosage_entry = tk.Entry(self.root)
        self.dosage_entry.pack()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        
        
        tk.Button(frame, text="επιλογή", command=self.chooseMedicine).grid(row=0, column=0, padx=5)

    def chooseMedicine(self):
        medicine = self.selected_medicine.get()
        dosage = self.dosage_entry.get().strip()
        self.controller.checkDosage(medicine, dosage)

    @staticmethod
    def redirectToMedicineScreen(root):
        root.destroy()

class CreatePrescriptionScreen:
    def __init__(self, root, medicine, dosage, controller):
        self.root = root
        self.controller = controller
        self.medicine = medicine
        self.dosage = dosage
        self.displayChoosenPrescription()

    def displayChoosenPrescription(self):
        self.root.title("Επιτυχής Συνταγογράφηση")

        tk.Label(self.root, text="Θέλετε να αποθηκεύσετε τη συνταγή;").pack(pady=10)
        tk.Label(self.root, text=f"{self.medicine} - {self.dosage}").pack(pady=5)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        
        tk.Button(frame, text="Αποθήκευση", command=self.accept_prescription).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Ακύρωση", command=self.reject_prescription).grid(row=0, column=1, padx=5)
    
    def accept_prescription(self):
        self.controller.acceptOrRejectPrescription(self.medicine, self.dosage, True)
        self.root.destroy()
    
    def reject_prescription(self):
        self.controller.acceptOrRejectPrescription(self.medicine, self.dosage, False)
        self.root.destroy()


class Message11Screen:
    def __init__(self, root):
        self.root = root
        self.displayNoDosageMessage()
    
    def displayNoDosageMessage(self):
        self.root.title("Απόρριψη Συνταγής")
        tk.Label(self.root, text="Δεν έχει εισαχθεί δοσολογία.").pack(pady=10)
        tk.Button(self.root, text="Επιστροφή", command=lambda: MedicineScreen.redirectToMedicineScreen(self.root)).pack(pady=5)


class RejectPrescriptionScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Ακύρωση Συνταγής")
        tk.Label(self.root, text="Η συνταγή ακυρώθηκε.").pack(pady=10)
        tk.Button(self.root, text="Επιστροφή", command=lambda: self.confirm(ok=True)).pack(pady=5)


    def confirm(self, ok):
        if ok:
            return MedicineScreen.redirectToMedicineScreen(self.root)



if __name__ == "__main__":
    import presMed 
    root = tk.Tk()
    controller = presMed.PrescriptionController()
    import parent
    parent_dict = {
        "Μαρία Παπαδοπούλου": parent.Parent(1, "Μαρία", "Παπαδοπούλου")
    }

    controller.showMedicineScreen(root, parent_dict)
    root.mainloop()