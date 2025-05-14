from tkinter import *
from tkinter import ttk
import sqlite3

class DoctorAppointmentManagement:
    def __init__(self, root):
        self.root = root
        self.root.title('Appointment Management Window')
        self.root.iconbitmap('C:/Users/Andreas/Documents/GitHub/Software-Engineering-Project-CEID/code/favicon.ico')

        self.setup_ui()
        self.load_appointments()

    def setup_ui(self):
        topframe = LabelFrame(self.root, text="this is the top frame", padx=200, pady=5)
        topframe.grid(row=0, column=0)

        Button(topframe, text="Home").grid(row=0, column=1)
        Button(topframe, text="Refresh", command=self.refresh_tree).grid(row=0, column=0)
        Button(topframe, text="Close", command=self.root.destroy).grid(row=0, column=2)

        self.tree = ttk.Treeview(self.root, columns=("Patient Name", "Date", "Status"), show="headings")
        self.tree.heading("Patient Name", text="Patient Name")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Status", text="Status")
        self.tree.grid(row=1, column=0)

        Button(self.root, text="Edit Appointment", command=self.edit_appointment).grid(row=2, column=0, pady=10)

    def load_appointments(self):
        conn = sqlite3.connect('hellobaby_database.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM appointments ORDER BY status")
        records = c.fetchall()
        for record in records:
            self.tree.insert("", "end", values=(record[0], record[1], record[2]))
        conn.close()

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.load_appointments()

    def edit_appointment(self):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, 'values')

        edit_win = Toplevel()
        edit_win.title("Edit Appointment")

        Label(edit_win, text="Patient Name").grid(row=0, column=0)
        patient_entry = Entry(edit_win)
        patient_entry.grid(row=0, column=1)
        patient_entry.insert(0, values[0])

        Label(edit_win, text="Date").grid(row=1, column=0)
        date_entry = Entry(edit_win)
        date_entry.grid(row=1, column=1)
        date_entry.insert(0, values[1])

        Label(edit_win, text="Status").grid(row=2, column=0)
        status_entry = Entry(edit_win)
        status_entry.grid(row=2, column=1)
        status_entry.insert(0, values[2])

        def save_changes():
            conn = sqlite3.connect('hellobaby_database.db')
            c = conn.cursor()
            c.execute("""UPDATE appointments SET 
                patient_name = ?, 
                date = ?, 
                status = ?
                WHERE rowid = ?
            """, (patient_entry.get(), date_entry.get(), status_entry.get(), self.tree.index(selected) + 1))
            conn.commit()
            conn.close()

            Label(edit_win, text="Sending update to parent...", fg="green").grid(row=4, column=0, columnspan=2, pady=10)
            save_btn.config(state="disabled")
            edit_win.after(2000, lambda: (edit_win.destroy(), self.refresh_tree()))

        save_btn = Button(edit_win, text="Save Changes", command=save_changes)
        save_btn.grid(row=3, column=0, columnspan=2)

# --- Launch the application ---
if __name__ == "__main__":
    root = Tk()
    app = DoctorAppointmentManagement(root)
    root.mainloop()
