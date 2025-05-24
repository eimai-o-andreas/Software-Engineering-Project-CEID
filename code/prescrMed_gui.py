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