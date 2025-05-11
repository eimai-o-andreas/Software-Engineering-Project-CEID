# Updated version of the seminar management code with display of existing seminars
import tkinter as tk
from tkinter import messagebox, simpledialog

class Seminar:
    def __init__(self, title, description, audience, room=None, datetime=None):
        self.title = title
        self.description = description
        self.audience = audience
        self.room = room
        self.datetime = datetime

    def __str__(self):
        info = f"Τίτλος: {self.title}\nΠεριγραφή: {self.description}\nΑπευθύνεται σε: {self.audience}"
        if self.room and self.datetime:
            info += f"\nΑίθουσα: {self.room}\nΗμερομηνία & Ώρα: {self.datetime}"
        return info

class SeminarManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Διαχείριση Σεμιναρίων")

         # Dummy data
         # List to store seminars
        self.seminars = [
            {"title": "Σεμινάριο 1", "description": "Πρώτο σεμινάριο", "audience": "Γονείς", "room": "Αίθουσα 1", "datetime": "2025-05-10 10:00"},
            {"title": "Σεμινάριο 2", "description": "Δεύτερο σεμινάριο", "audience": "Ιατροί", "room": "Αίθουσα 2", "datetime": "2025-05-12 14:00"}
        ]


        self.available_rooms = {
            "Αίθουσα 1": ["2025-04-30 10:00", "2025-04-30 12:00"],
            "Αίθουσα 2": ["2025-05-01 09:00", "2025-05-01 11:00"],
        }

        self.show_main_menu()

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Υπάρχοντα Σεμινάρια:", font=("Arial", 14)).pack(pady=10)
        for seminar in self.seminars:
            frame = tk.Frame(self.root)
            frame.pack(pady=5, fill='x', padx=10)
            tk.Label(frame, text=f"{seminar['title']} - {seminar['datetime']}").pack(side='left')
            tk.Button(frame, text="Πληροφορίες", command=lambda s=seminar: self.view_info(s)).pack(side='right')
            tk.Button(frame, text="Τροποποίηση", command=lambda s=seminar: self.modify_seminar(s)).pack(side='right')
            tk.Button(frame, text="Ακύρωση", command=lambda s=seminar: self.cancel_seminar(s)).pack(side='right')

        tk.Button(self.root, text="Προσθήκη Σεμιναρίου", command=self.add_seminar_screen).pack(pady=5)
        
    def view_info(self, seminar):
        info = f"Τίτλος: {seminar['title']}\nΠεριγραφή: {seminar['description']}\nΑπευθύνεται σε: {seminar['audience']}\nΑίθουσα: {seminar['room']}\nΗμερομηνία και Ώρα: {seminar['datetime']}"
        messagebox.showinfo("Πληροφορίες Σεμιναρίου", info)

    def modify_seminar(self, seminar):
        room = simpledialog.askstring("Αλλαγή Αίθουσας", "Νέα Αίθουσα:", initialvalue=seminar['room'])
        if room and room in self.available_rooms:
            options = self.available_rooms[room]
            new_dt = simpledialog.askstring("Αλλαγή Ημερομηνίας/Ώρας", f"Επιλέξτε ημερομηνία/ώρα: {options}", initialvalue=options[0])
            if new_dt in options:
                seminar['room'] = room
                seminar['datetime'] = new_dt
                messagebox.showinfo("Επιτυχία", "Το σεμινάριο τροποποιήθηκε.")
                self.create_main_menu()

    def cancel_seminar(self, seminar):
        confirm = messagebox.askyesno("Επιβεβαίωση", f"Θέλετε να ακυρώσετε το '{seminar['title']}'?")
        if confirm:
            self.seminars.remove(seminar)
            messagebox.showinfo("Ακύρωση", "Το σεμινάριο ακυρώθηκε.")
            self.create_main_menu()


    def add_seminar_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Καταχώριση Στοιχείων Σεμιναρίου", font=('Helvetica', 14)).pack(pady=10)
        self.title_entry = tk.Entry(self.root, width=40)
        self.desc_entry = tk.Entry(self.root, width=40)
        self.audience_entry = tk.Entry(self.root, width=40)
        tk.Label(self.root, text="Τίτλος:").pack()
        self.title_entry.pack()
        tk.Label(self.root, text="Περιγραφή:").pack()
        self.desc_entry.pack()
        tk.Label(self.root, text="Απευθύνεται σε:").pack()
        self.audience_entry.pack()
        tk.Button(self.root, text="Συνέχεια", command=self.choose_room_screen).pack(pady=10)

    def choose_room_screen(self):
        self.new_seminar = Seminar(
            self.title_entry.get(),
            self.desc_entry.get(),
            self.audience_entry.get()
        )

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Επιλογή Διαθέσιμης Αίθουσας", font=('Helvetica', 14)).pack(pady=10)
        self.selected_room = tk.StringVar()
        self.selected_room.set(list(self.available_rooms.keys())[0])
        tk.OptionMenu(self.root, self.selected_room, *self.available_rooms.keys()).pack()
        tk.Button(self.root, text="Συνέχεια", command=self.choose_datetime_screen).pack(pady=10)

    def choose_datetime_screen(self):
        selected = self.selected_room.get()
        self.new_seminar.room = selected

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Επιλογή Διαθέσιμης Ημερομηνίας και Ώρας", font=('Helvetica', 14)).pack(pady=10)
        self.selected_datetime = tk.StringVar()
        self.selected_datetime.set(self.available_rooms[selected][0])
        tk.OptionMenu(self.root, self.selected_datetime, *self.available_rooms[selected]).pack()
        tk.Button(self.root, text="Καταχώριση Σεμιναρίου", command=self.save_seminar).pack(pady=10)

    def save_seminar(self):
        self.new_seminar.datetime = self.selected_datetime.get()
        self.seminars.append(self.new_seminar)
        # Remove the selected date/time from available list
        self.available_rooms[self.new_seminar.room].remove(self.new_seminar.datetime)
        messagebox.showinfo("Επιτυχία", "Το σεμινάριο καταχωρήθηκε με επιτυχία.")
        self.show_main_menu()

    def view_seminars_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Υπάρχοντα Σεμινάρια", font=('Helvetica', 14)).pack(pady=10)
        for seminar in self.seminars:
            tk.Label(self.root, text=str(seminar), justify="left", wraplength=400, relief="groove", padx=5, pady=5).pack(pady=5, fill="x")
        tk.Button(self.root, text="Επιστροφή", command=self.show_main_menu).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SeminarManagerApp(root)
    root.mainloop()
