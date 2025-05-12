from tkinter import *
from tkinter import ttk
import sqlite3




#doctor's appointment managment
def doc_appointment_open():
    doc_appointment = Toplevel()
    doc_appointment.title('Appointment Management Window')
    doc_appointment.iconbitmap('C:/Users/Andreas/Documents/GitHub/Software-Engineering-Project-CEID/code/favicon.ico')    

    topframe = LabelFrame(doc_appointment, text="this is the top frame", padx=200, pady=5)
    topframe.grid(row=0, column=0)
    HomeButton = Button(topframe, text="Home")
    HomeButton.grid(row=0, column=1)
    refreshbutton = Button(topframe, text="Refresh", command=lambda: refresh_tree(tree))
    refreshbutton.grid(row=0, column=0)
    close_button = Button(topframe, text="Close", command=doc_appointment.destroy)
    close_button.grid(row=0, column=2)

    #show appointments from database
    tree = ttk.Treeview(doc_appointment, columns=("Patient Name", "Date", "Status"), show="headings")
    tree.heading("Patient Name", text="Patient Name")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")
    tree.grid(row=1, column=0)

    conn = sqlite3.connect('hellobaby_database.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM appointments ORDER BY status")
    records = c.fetchall()
    for record in records:
        tree.insert("", "end", values=(record[0], record[1], record[2]))
    conn.close()

    #edit buttons
    edit_btn = Button(doc_appointment, text="Edit Appointment", command=lambda: edit_appointment(tree))
    edit_btn.grid(row=2, column=0, pady=10)


#appointment editing window
def edit_appointment(tree):
    selected = tree.focus()
    if not selected:
        return  # no selection
    values = tree.item(selected, 'values')

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
        """, (patient_entry.get(), date_entry.get(), status_entry.get(), tree.index(selected)+1))
        conn.commit()
        conn.close()

        # Show "Sending update to parent..." label
        sending_label = Label(edit_win, text="Sending update to parent...", fg="green")
        sending_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Disable the Save button (optional, to prevent clicking again)
        save_btn.config(state="disabled")

        # After 2 seconds, close the edit window and refresh the tree
        edit_win.after(2000, lambda: (edit_win.destroy(), refresh_tree(tree)))

    save_btn = Button(edit_win, text="Save Changes", command=save_changes)
    save_btn.grid(row=3, column=0, columnspan=2)

def refresh_tree(tree):
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect('hellobaby_database.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM appointments")
    records = c.fetchall()
    for record in records:
        tree.insert("", "end", values=(record[0], record[1], record[2]))
    conn.close()




doc_appointment = Tk()
doc_appointment.title('Appointment Management Window')
doc_appointment.iconbitmap('C:/Users/Andreas/Documents/GitHub/Software-Engineering-Project-CEID/code/favicon.ico')    

topframe = LabelFrame(doc_appointment, text="this is the top frame", padx=200, pady=5)
topframe.grid(row=0, column=0)
HomeButton = Button(topframe, text="Home")
HomeButton.grid(row=0, column=1)
refreshbutton = Button(topframe, text="Refresh", command=lambda: refresh_tree(tree))
refreshbutton.grid(row=0, column=0)
close_button = Button(topframe, text="Close", command=doc_appointment.destroy)
close_button.grid(row=0, column=2)

#show appointments from database
tree = ttk.Treeview(doc_appointment, columns=("Patient Name", "Date", "Status"), show="headings")
tree.heading("Patient Name", text="Patient Name")
tree.heading("Date", text="Date")
tree.heading("Status", text="Status")
tree.grid(row=1, column=0)

conn = sqlite3.connect('hellobaby_database.db')
c = conn.cursor()
c.execute("SELECT *, oid FROM appointments ORDER BY status")
records = c.fetchall()
for record in records:
    tree.insert("", "end", values=(record[0], record[1], record[2]))
conn.close()

#edit buttons
edit_btn = Button(doc_appointment, text="Edit Appointment", command=lambda: edit_appointment(tree))
edit_btn.grid(row=2, column=0, pady=10)


#database setup
conn = sqlite3.connect('hellobaby_database.db')
c = conn.cursor()

#parent is supposed to add these to the database:
#c.execute("""INSERT INTO appointments (patient_name, date, status)
#             VALUES (:patient_name, :date, :status)""",
#          {
#              'patient_name': 'eleni',
#              'date': '15-12-2025',
#              'status': 'rejected',
#          })

conn.commit()
conn.close()


root.mainloop()

