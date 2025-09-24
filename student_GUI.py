import tkinter as tk
from tkinter import ttk, messagebox

class Student:
    def __init__(self, roll, name, course, semester, subjects, marks, attendance):
        self.roll = roll
        self.name = name
        self.course = course
        self.semester = semester
        self.subjects = subjects  # dict: {subject: type}
        self.marks = marks        # dict: {subject: [C1, C2, C3, C4]}
        self.attendance = attendance  # dict: {subject: %}
        self.grades = {}          # dict: {subject: (grade, grade_point)}
        self.cgpa = 0.0

    def compute_grades(self):
        total_points = 0
        count = 0
        for subject, comps in self.marks.items():
            total = sum(comps)
            if total >= 90:
                grade, gp = 'S', 10
            elif total >= 80:
                grade, gp = 'A', 9
            elif total >= 70:
                grade, gp = 'B', 8
            elif total >= 60:
                grade, gp = 'C', 7
            elif total >= 50:
                grade, gp = 'D', 6
            else:
                grade, gp = 'F', 0
            self.grades[subject] = (grade, gp)
            total_points += gp
            count += 1
        self.cgpa = round(total_points / count, 2) if count else 0.0

students = []

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    subjects = {
        hc_entry.get(): 'Hardcore',
        sc_entry.get(): 'Softcore',
        oe_entry.get(): 'Open Elective'
    }
    marks = {
        hc_entry.get(): [int(c1_hc.get()), int(c2_hc.get()), int(c3_hc.get()), int(c4_hc.get())],
        sc_entry.get(): [int(c1_sc.get()), int(c2_sc.get()), int(c3_sc.get()), int(c4_sc.get())],
        oe_entry.get(): [int(c1_oe.get()), int(c2_oe.get()), int(c3_oe.get()), int(c4_oe.get())]
    }
    attendance = {
        hc_entry.get(): int(att_hc.get()),
        sc_entry.get(): int(att_sc.get()),
        oe_entry.get(): int(att_oe.get())
    }
    s = Student(roll, name, course, semester, subjects, marks, attendance)
    s.compute_grades()
    students.append(s)
    messagebox.showinfo("Success", f"Student {name} added with CGPA {s.cgpa}")

def list_all():
    output.delete(1.0, tk.END)
    for s in students:
        output.insert(tk.END, f"{s.roll} | {s.name} | CGPA: {s.cgpa}\n")

root = tk.Tk()
root.title("M.Sc. Student Info System")

# --- Student Info ---
tk.Label(root, text="Roll No").grid(row=0, column=0); roll_entry = tk.Entry(root); roll_entry.grid(row=0, column=1)
tk.Label(root, text="Name").grid(row=1, column=0); name_entry = tk.Entry(root); name_entry.grid(row=1, column=1)
tk.Label(root, text="Course").grid(row=2, column=0); course_entry = tk.Entry(root); course_entry.grid(row=2, column=1)
tk.Label(root, text="Semester").grid(row=3, column=0); semester_entry = tk.Entry(root); semester_entry.grid(row=3, column=1)

# --- Subjects ---
tk.Label(root, text="Hardcore Subject").grid(row=4, column=0); hc_entry = tk.Entry(root); hc_entry.grid(row=4, column=1)
tk.Label(root, text="Softcore Subject").grid(row=5, column=0); sc_entry = tk.Entry(root); sc_entry.grid(row=5, column=1)
tk.Label(root, text="Open Elective").grid(row=6, column=0); oe_entry = tk.Entry(root); oe_entry.grid(row=6, column=1)

# --- Marks ---
tk.Label(root, text="C1 HC").grid(row=7, column=0); c1_hc = tk.Entry(root); c1_hc.grid(row=7, column=1)
tk.Label(root, text="C2 HC").grid(row=8, column=0); c2_hc = tk.Entry(root); c2_hc.grid(row=8, column=1)
tk.Label(root, text="C3 HC").grid(row=9, column=0); c3_hc = tk.Entry(root); c3_hc.grid(row=9, column=1)
tk.Label(root, text="C4 HC").grid(row=10, column=0); c4_hc = tk.Entry(root); c4_hc.grid(row=10, column=1)

tk.Label(root, text="C1 SC").grid(row=7, column=2); c1_sc = tk.Entry(root); c1_sc.grid(row=7, column=3)
tk.Label(root, text="C2 SC").grid(row=8, column=2); c2_sc = tk.Entry(root); c2_sc.grid(row=8, column=3)
tk.Label(root, text="C3 SC").grid(row=9, column=2); c3_sc = tk.Entry(root); c3_sc.grid(row=9, column=3)
tk.Label(root, text="C4 SC").grid(row=10, column=2); c4_sc = tk.Entry(root); c4_sc.grid(row=10, column=3)

tk.Label(root, text="C1 OE").grid(row=7, column=4); c1_oe = tk.Entry(root); c1_oe.grid(row=7, column=5)
tk.Label(root, text="C2 OE").grid(row=8, column=4); c2_oe = tk.Entry(root); c2_oe.grid(row=8, column=5)
tk.Label(root, text="C3 OE").grid(row=9, column=4); c3_oe = tk.Entry(root); c3_oe.grid(row=9, column=5)
tk.Label(root, text="C4 OE").grid(row=10, column=4); c4_oe = tk.Entry(root); c4_oe.grid(row=10, column=5)

# --- Attendance ---
tk.Label(root, text="Attendance HC").grid(row=11, column=0); att_hc = tk.Entry(root); att_hc.grid(row=11, column=1)
tk.Label(root, text="Attendance SC").grid(row=11, column=2); att_sc = tk.Entry(root); att_sc.grid(row=11, column=3)
tk.Label(root, text="Attendance OE").grid(row=11, column=4); att_oe = tk.Entry(root); att_oe.grid(row=11, column=5)

# --- Buttons ---
tk.Button(root, text="Add Student", command=add_student).grid(row=12, column=0, columnspan=2)
tk.Button(root, text="List All Students", command=list_all).grid(row=12, column=2, columnspan=2)

# --- Output ---
output = tk.Text(root, height=10, width=80)
output.grid(row=13, column=0, columnspan=6)

root.mainloop()
