import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import pymysql
from datetime import datetime

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'Prnsh@0303'
DB_NAME = 'EduSchema'

# Establish the database connection
try:
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Prnsh@0303",
        database="EduSchema"
    )
    # config.py
    cursor = db_connection.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    messagebox.showerror("Database Connection Error", f"Error: {err}")
    exit(1)

# Utility functions
def fetch_data(table):
    cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()

def refresh_table(table, tree):
    for row in tree.get_children():
        tree.delete(row)
    for record in fetch_data(table):
        tree.insert("", tk.END, values=record)

# Clear entry fields
def clear_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)

# Add Course
def add_course():
    course_name = course_name_entry.get()
    course_description = course_description_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    if course_name and start_date and end_date:
        try:
            cursor.execute("INSERT INTO Courses (course_name, course_description, start_date, end_date) VALUES (%s, %s, %s, %s)", (course_name, course_description, start_date, end_date))
            db_connection.commit()
            refresh_table("Courses", course_tree)
            clear_entries([course_name_entry, course_description_entry, start_date_entry, end_date_entry])
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all mandatory fields")

# Delete Course with Backup
def delete_course():
    selected_item = course_tree.selection()
    if selected_item:
        course_id = course_tree.item(selected_item[0])['values'][0]
        try:
            cursor.execute("INSERT INTO Backup_Courses SELECT * FROM Courses WHERE course_id = %s", (course_id,))
            cursor.execute("DELETE FROM Courses WHERE course_id = %s", (course_id,))
            db_connection.commit()
            refresh_table("Courses", course_tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select a course to delete")

# Add Instructor
def add_instructor():
    first_name = instructor_first_name_entry.get()
    last_name = instructor_last_name_entry.get()
    email = instructor_email_entry.get()
    phone = instructor_phone_entry.get()
    if first_name and last_name and email:
        try:
            cursor.execute("INSERT INTO Instructors (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, phone))
            db_connection.commit()
            refresh_table("Instructors", instructor_tree)
            clear_entries([instructor_first_name_entry, instructor_last_name_entry, instructor_email_entry])
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all mandatory fields")

# Delete Instructor with Backup
def delete_instructor():
    selected_item = instructor_tree.selection()
    if selected_item:
        instructor_id = instructor_tree.item(selected_item[0])['values'][0]
        try:
            cursor.execute("INSERT INTO Backup_Instructors SELECT * FROM Instructors WHERE instructor_id = %s", (instructor_id,))
            cursor.execute("DELETE FROM Instructors WHERE instructor_id = %s", (instructor_id,))
            db_connection.commit()
            refresh_table("Instructors", instructor_tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select an instructor to delete")

# Add Student
def add_student():
    first_name = student_first_name_entry.get()
    last_name = student_last_name_entry.get()
    email = student_email_entry.get()
    phone = student_phone_entry.get()
    if first_name and last_name and email:
        try:
            cursor.execute("INSERT INTO Students (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, phone))
            db_connection.commit()
            refresh_table("Students", student_tree)
            clear_entries([student_first_name_entry, student_last_name_entry, student_email_entry, student_phone_entry])
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all mandatory fields")

# Delete Student with Backup
def delete_student():
    selected_item = student_tree.selection()
    if selected_item:
        student_id = student_tree.item(selected_item[0])['values'][0]
        try:
            cursor.execute("INSERT INTO Backup_Students SELECT * FROM Students WHERE student_id = %s", (student_id,))
            cursor.execute("DELETE FROM Students WHERE student_id = %s", (student_id,))
            db_connection.commit()
            refresh_table("Students", student_tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select a student to delete")

# Add Enrollment
def add_enrollment():
    student_id = enrollment_student_id_entry.get()
    course_id = enrollment_course_id_entry.get()
    enrollment_date = enrollment_date_entry.get()
    if student_id and course_id and enrollment_date:
        try:
            cursor.execute("INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)", (student_id, course_id, enrollment_date))
            db_connection.commit()
            refresh_table("Enrollments", enrollment_tree)
            clear_entries([enrollment_student_id_entry, enrollment_course_id_entry, enrollment_date_entry])
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all mandatory fields")

# Delete Enrollment with Backup
def delete_enrollment():
    selected_item = enrollment_tree.selection()
    if selected_item:
        enrollment_id = enrollment_tree.item(selected_item[0])['values'][0]
        try:
            cursor.execute("INSERT INTO Backup_Enrollments SELECT * FROM Enrollments WHERE enrollment_id = %s", (enrollment_id,))
            cursor.execute("DELETE FROM Enrollments WHERE enrollment_id = %s", (enrollment_id,))
            db_connection.commit()
            refresh_table("Enrollments", enrollment_tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select an enrollment to delete")

# Add Assessment
def add_assessment():
    course_id = assessment_course_id_entry.get()
    assessment_name = assessment_name_entry.get()
    due_date = assessment_due_date_entry.get()
    if course_id and assessment_name and due_date:
        try:
            cursor.execute("INSERT INTO Assessments (course_id, assessment_name, due_date) VALUES (%s, %s, %s)", (course_id, assessment_name, due_date))
            db_connection.commit()
            refresh_table("Assessments", assessment_tree)
            clear_entries([assessment_course_id_entry, assessment_name_entry, assessment_due_date_entry])
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all mandatory fields")

# Delete Assessment with Backup
def delete_assessment():
    selected_item = assessment_tree.selection()
    if selected_item:
        assessment_id = assessment_tree.item(selected_item[0])['values'][0]
        try:
            cursor.execute("INSERT INTO Backup_Assessments SELECT * FROM Assessments WHERE assessment_id = %s", (assessment_id,))
            cursor.execute("DELETE FROM Assessments WHERE assessment_id = %s", (assessment_id,))
            db_connection.commit()
            refresh_table("Assessments", assessment_tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select an assessment to delete")

# Add Grade
def add_grade():
    enrollment_id = grade_enrollment_id_entry.get()
    assessment_id = grade_assessment_id_entry.get()
    grade = grade_entry.get()
    if enrollment_id and assessment_id and grade:
        try:
            cursor.execute("INSERT INTO Grades (enrollment_id, assessment_id, grade) VALUES (%s, %s, %s)", (enrollment_id, assessment_id, grade))
            db_connection.commit()
            refresh_table("Grades", grade_tree)
            clear_entries([grade_enrollment_id_entry, grade_assessment_id_entry, grade_entry])
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all mandatory fields")

# Delete Grade with Backup
def delete_grade():
    selected_item = grade_tree.selection()
    if selected_item:
        grade_id = grade_tree.item(selected_item[0])['values'][0]
        try:
            cursor.execute("INSERT INTO Backup_Grades SELECT * FROM Grades WHERE grade_id = %s", (grade_id,))
            cursor.execute("DELETE FROM Grades WHERE grade_id = %s", (grade_id,))
            db_connection.commit()
            refresh_table("Grades", grade_tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select a grade to delete")

# GUI setup
root = tk.Tk()
root.title("EduSchema Management System")
root.geometry("1200x800")
root.configure(bg="black")

# Create tabs
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")

# Courses Tab
course_tab = ttk.Frame(tab_control)
tab_control.add(course_tab, text='Courses')

course_frame = ttk.LabelFrame(course_tab, text="Course Details")
course_frame.pack(fill="both", expand="yes", padx=10, pady=10)

course_name_label = ttk.Label(course_frame, text="Course Name:")
course_name_label.grid(row=0, column=0, padx=5, pady=5)
course_name_entry = ttk.Entry(course_frame)
course_name_entry.grid(row=0, column=1, padx=5, pady=5)

course_description_label = ttk.Label(course_frame, text="Course Description:")
course_description_label.grid(row=1, column=0, padx=5, pady=5)
course_description_entry = ttk.Entry(course_frame)
course_description_entry.grid(row=1, column=1, padx=5, pady=5)

start_date_label = ttk.Label(course_frame, text="Start Date (YYYY-MM-DD):")
start_date_label.grid(row=2, column=0, padx=5, pady=5)
start_date_entry = ttk.Entry(course_frame)
start_date_entry.grid(row=2, column=1, padx=5, pady=5)

end_date_label = ttk.Label(course_frame, text="End Date (YYYY-MM-DD):")
end_date_label.grid(row=3, column=0, padx=5, pady=5)
end_date_entry = ttk.Entry(course_frame)
end_date_entry.grid(row=3, column=1, padx=5, pady=5)

add_course_button = ttk.Button(course_frame, text="Add Course", command=add_course)
add_course_button.grid(row=4, column=0, padx=5, pady=5)

delete_course_button = ttk.Button(course_frame, text="Delete Course", command=delete_course)
delete_course_button.grid(row=4, column=1, padx=5, pady=5)

course_tree = ttk.Treeview(course_tab, columns=("ID", "Name", "Description", "Start Date", "End Date"), show="headings")
course_tree.heading("ID", text="ID")
course_tree.heading("Name", text="Name")
course_tree.heading("Description", text="Description")
course_tree.heading("Start Date", text="Start Date")
course_tree.heading("End Date", text="End Date")
course_tree.pack(fill="both", expand="yes", padx=10, pady=10)

refresh_table("Courses", course_tree)

# Instructors Tab
instructor_tab = ttk.Frame(tab_control)
tab_control.add(instructor_tab, text='Instructors')

instructor_frame = ttk.LabelFrame(instructor_tab, text="Instructor Details")
instructor_frame.pack(fill="both", expand="yes", padx=10, pady=10)

instructor_first_name_label = ttk.Label(instructor_frame, text="First Name:")
instructor_first_name_label.grid(row=0, column=0, padx=5, pady=5)
instructor_first_name_entry = ttk.Entry(instructor_frame)
instructor_first_name_entry.grid(row=0, column=1, padx=5, pady=5)

instructor_last_name_label = ttk.Label(instructor_frame, text="Last Name:")
instructor_last_name_label.grid(row=1, column=0, padx=5, pady=5)
instructor_last_name_entry = ttk.Entry(instructor_frame)
instructor_last_name_entry.grid(row=1, column=1, padx=5, pady=5)

instructor_email_label = ttk.Label(instructor_frame, text="Email:")
instructor_email_label.grid(row=2, column=0, padx=5, pady=5)
instructor_email_entry = ttk.Entry(instructor_frame)
instructor_email_entry.grid(row=2, column=1, padx=5, pady=5)

instructor_phone_label = ttk.Label(instructor_frame, text="Phone:")
instructor_phone_label.grid(row=3, column=0, padx=5, pady=5)
instructor_phone_entry = ttk.Entry(instructor_frame)
instructor_phone_entry.grid(row=3, column=1, padx=5, pady=5)

add_instructor_button = ttk.Button(instructor_frame, text="Add Instructor", command=add_instructor)
add_instructor_button.grid(row=4, column=0, padx=5, pady=5)

delete_instructor_button = ttk.Button(instructor_frame, text="Delete Instructor", command=delete_instructor)
delete_instructor_button.grid(row=4, column=1, padx=5, pady=5)

instructor_tree = ttk.Treeview(instructor_tab, columns=("ID", "First Name", "Last Name", "Email", "Phone"), show="headings")
instructor_tree.heading("ID", text="ID")
instructor_tree.heading("First Name", text="First Name")
instructor_tree.heading("Last Name", text="Last Name")
instructor_tree.heading("Email", text="Email")
instructor_tree.heading("Phone", text="Phone")
instructor_tree.pack(fill="both", expand="yes", padx=10, pady=10)

refresh_table("Instructors", instructor_tree)

# Students Tab
student_tab = ttk.Frame(tab_control)
tab_control.add(student_tab, text='Students')

student_frame = ttk.LabelFrame(student_tab, text="Student Details")
student_frame.pack(fill="both", expand="yes", padx=10, pady=10)

student_first_name_label = ttk.Label(student_frame, text="First Name:")
student_first_name_label.grid(row=0, column=0, padx=5, pady=5)
student_first_name_entry = ttk.Entry(student_frame)
student_first_name_entry.grid(row=0, column=1, padx=5, pady=5)

student_last_name_label = ttk.Label(student_frame, text="Last Name:")
student_last_name_label.grid(row=1, column=0, padx=5, pady=5)
student_last_name_entry = ttk.Entry(student_frame)
student_last_name_entry.grid(row=1, column=1, padx=5, pady=5)

student_email_label = ttk.Label(student_frame, text="Email:")
student_email_label.grid(row=2, column=0, padx=5, pady=5)
student_email_entry = ttk.Entry(student_frame)
student_email_entry.grid(row=2, column=1, padx=5, pady=5)

student_phone_label = ttk.Label(student_frame, text="Phone:")
student_phone_label.grid(row=3, column=0, padx=5, pady=5)
student_phone_entry = ttk.Entry(student_frame)
student_phone_entry.grid(row=3, column=1, padx=5, pady=5)

add_student_button = ttk.Button(student_frame, text="Add Student", command=add_student)
add_student_button.grid(row=4, column=0, padx=5, pady=5)

delete_student_button = ttk.Button(student_frame, text="Delete Student", command=delete_student)
delete_student_button.grid(row=4, column=1, padx=5, pady=5)

student_tree = ttk.Treeview(student_tab, columns=("ID", "First Name", "Last Name", "Email", "Phone"), show="headings")
student_tree.heading("ID", text="ID")
student_tree.heading("First Name", text="First Name")
student_tree.heading("Last Name", text="Last Name")
student_tree.heading("Email", text="Email")
student_tree.heading("Phone", text="Phone")
student_tree.pack(fill="both", expand="yes", padx=10, pady=10)

refresh_table("Students", student_tree)

# Enrollments Tab
enrollment_tab = ttk.Frame(tab_control)
tab_control.add(enrollment_tab, text='Enrollments')

enrollment_frame = ttk.LabelFrame(enrollment_tab, text="Enrollment Details")
enrollment_frame.pack(fill="both", expand="yes", padx=10, pady=10)

enrollment_student_id_label = ttk.Label(enrollment_frame, text="Student ID:")
enrollment_student_id_label.grid(row=0, column=0, padx=5, pady=5)
enrollment_student_id_entry = ttk.Entry(enrollment_frame)
enrollment_student_id_entry.grid(row=0, column=1, padx=5, pady=5)

enrollment_course_id_label = ttk.Label(enrollment_frame, text="Course ID:")
enrollment_course_id_label.grid(row=1, column=0, padx=5, pady=5)
enrollment_course_id_entry = ttk.Entry(enrollment_frame)
enrollment_course_id_entry.grid(row=1, column=1, padx=5, pady=5)

enrollment_date_label = ttk.Label(enrollment_frame, text="Enrollment Date (YYYY-MM-DD):")
enrollment_date_label.grid(row=2, column=0, padx=5, pady=5)
enrollment_date_entry = ttk.Entry(enrollment_frame)
enrollment_date_entry.grid(row=2, column=1, padx=5, pady=5)

add_enrollment_button = ttk.Button(enrollment_frame, text="Add Enrollment", command=add_enrollment)
add_enrollment_button.grid(row=3, column=0, padx=5, pady=5)

delete_enrollment_button = ttk.Button(enrollment_frame, text="Delete Enrollment", command=delete_enrollment)
delete_enrollment_button.grid(row=3, column=1, padx=5, pady=5)

enrollment_tree = ttk.Treeview(enrollment_tab, columns=("ID", "Student ID", "Course ID", "Enrollment Date"), show="headings")
enrollment_tree.heading("ID", text="ID")
enrollment_tree.heading("Student ID", text="Student ID")
enrollment_tree.heading("Course ID", text="Course ID")
enrollment_tree.heading("Enrollment Date", text="Enrollment Date")
enrollment_tree.pack(fill="both", expand="yes", padx=10, pady=10)

refresh_table("Enrollments", enrollment_tree)

# Assessments Tab
assessment_tab = ttk.Frame(tab_control)
tab_control.add(assessment_tab, text='Assessments')

assessment_frame = ttk.LabelFrame(assessment_tab, text="Assessment Details")
assessment_frame.pack(fill="both", expand="yes", padx=10, pady=10)

assessment_course_id_label = ttk.Label(assessment_frame, text="Course ID:")
assessment_course_id_label.grid(row=0, column=0, padx=5, pady=5)
assessment_course_id_entry = ttk.Entry(assessment_frame)
assessment_course_id_entry.grid(row=0, column=1, padx=5, pady=5)

assessment_name_label = ttk.Label(assessment_frame, text="Assessment Name:")
assessment_name_label.grid(row=1, column=0, padx=5, pady=5)
assessment_name_entry = ttk.Entry(assessment_frame)
assessment_name_entry.grid(row=1, column=1, padx=5, pady=5)

assessment_due_date_label = ttk.Label(assessment_frame, text="Due Date (YYYY-MM-DD):")
assessment_due_date_label.grid(row=2, column=0, padx=5, pady=5)
assessment_due_date_entry = ttk.Entry(assessment_frame)
assessment_due_date_entry.grid(row=2, column=1, padx=5, pady=5)

add_assessment_button = ttk.Button(assessment_frame, text="Add Assessment", command=add_assessment)
add_assessment_button.grid(row=3, column=0, padx=5, pady=5)

delete_assessment_button = ttk.Button(assessment_frame, text="Delete Assessment", command=delete_assessment)
delete_assessment_button.grid(row=3, column=1, padx=5, pady=5)

assessment_tree = ttk.Treeview(assessment_tab, columns=("ID", "Course ID", "Assessment Name", "Due Date"), show="headings")
assessment_tree.heading("ID", text="ID")
assessment_tree.heading("Course ID", text="Course ID")
assessment_tree.heading("Assessment Name", text="Assessment Name")
assessment_tree.heading("Due Date", text="Due Date")
assessment_tree.pack(fill="both", expand="yes", padx=10, pady=10)

refresh_table("Assessments", assessment_tree)

# Grades Tab
grade_tab = ttk.Frame(tab_control)
tab_control.add(grade_tab, text='Grades')

grade_frame = ttk.LabelFrame(grade_tab, text="Grade Details")
grade_frame.pack(fill="both", expand="yes", padx=10, pady=10)

grade_enrollment_id_label = ttk.Label(grade_frame, text="Enrollment ID:")
grade_enrollment_id_label.grid(row=0, column=0, padx=5, pady=5)
grade_enrollment_id_entry = ttk.Entry(grade_frame)
grade_enrollment_id_entry.grid(row=0, column=1, padx=5, pady=5)

grade_assessment_id_label = ttk.Label(grade_frame, text="Assessment ID:")
grade_assessment_id_label.grid(row=1, column=0, padx=5, pady=5)
grade_assessment_id_entry = ttk.Entry(grade_frame)
grade_assessment_id_entry.grid(row=1, column=1, padx=5, pady=5)

grade_label = ttk.Label(grade_frame, text="Grade:")
grade_label.grid(row=2, column=0, padx=5, pady=5)
grade_entry = ttk.Entry(grade_frame)
grade_entry.grid(row=2, column=1, padx=5, pady=5)

add_grade_button = ttk.Button(grade_frame, text="Add Grade", command=add_grade)
add_grade_button.grid(row=3, column=0, padx=5, pady=5)

delete_grade_button = ttk.Button(grade_frame, text="Delete Grade", command=delete_grade)
delete_grade_button.grid(row=3, column=1, padx=5, pady=5)

grade_tree = ttk.Treeview(grade_tab, columns=("ID", "Enrollment ID", "Assessment ID", "Grade"), show="headings")
grade_tree.heading("ID", text="ID")
grade_tree.heading("Enrollment ID", text="Enrollment ID")
grade_tree.heading("Assessment ID", text="Assessment ID")
grade_tree.heading("Grade", text="Grade")
grade_tree.pack(fill="both", expand="yes", padx=10, pady=10)

refresh_table("Grades", grade_tree)

# Backup Tab
backup_tab = ttk.Frame(tab_control)
tab_control.add(backup_tab, text='Backup')

backup_label = ttk.Label(backup_tab, text="Backup Tables", font=("Helvetica", 16))
backup_label.pack(pady=10)

backup_tree_frame = ttk.LabelFrame(backup_tab, text="Backup Tables")
backup_tree_frame.pack(fill="both", expand="yes", padx=10, pady=10)

backup_note = ttk.Label(backup_tree_frame, text="Select a backup table to view deleted records:", font=("Helvetica", 10))
backup_note.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

backup_tables = ["Backup_Courses", "Backup_Instructors", "Backup_Students", "Backup_Enrollments", "Backup_Assessments", "Backup_Grades"]
backup_table_var = tk.StringVar(value=backup_tables)
backup_table_listbox = tk.Listbox(backup_tree_frame, listvariable=backup_table_var, height=6)
backup_table_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def show_backup_records():
    selected_table = backup_table_listbox.get(tk.ACTIVE)
    try:
        cursor.execute(f"SELECT * FROM {selected_table}")
        records = cursor.fetchall()
        messagebox.showinfo(f"Backup Table: {selected_table}", "\n".join([str(record) for record in records]))
    except Exception as e:
        messagebox.showerror("Error", str(e))

show_backup_button = ttk.Button(backup_tree_frame, text="Show Backup Records", command=show_backup_records)
show_backup_button.grid(row=2, column=0, padx=5, pady=5)

clear_backup_button = ttk.Button(backup_tree_frame, text="Clear Backup Records", command=show_backup_records)
clear_backup_button.grid(row=2, column=1, padx=5, pady=5)

# Connect to Database
try:
    db_connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = db_connection.cursor()
except Exception as e:
    messagebox.showerror("Database Connection Error", str(e))
    root.destroy()

# Function to refresh tables
def refresh_table(table_name, tree_view):
    tree_view.delete(*tree_view.get_children())
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        for record in records:
            tree_view.insert("", tk.END, values=record)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main loop
root.mainloop()
