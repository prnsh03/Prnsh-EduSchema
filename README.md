# Prnsh-EduSchema
EduSchema Management System is an educational management tool built with Python and Tkinter, integrating with a MySQL database. It manages courses, instructors, students, enrollments, assessments, and grades, offering functionalities to add, delete, view records, and backup deleted data.

# EduSchema Management System

EduSchema Management System is a comprehensive educational management tool developed using Python and Tkinter for the graphical user interface. The system integrates with a MySQL database to manage various aspects of an educational institution including courses, instructors, students, enrollments, assessments, and grades. It offers functionality to add, delete, and view records in a user-friendly manner. The system also includes a backup feature for deleted records to prevent data loss.

## Features

1. **Course Management**
   - Add and delete courses
   - View course details

2. **Instructor Management**
   - Add and delete instructors
   - View instructor details

3. **Student Management**
   - Add and delete students
   - View student details

4. **Enrollment Management**
   - Add and delete enrollments
   - View enrollment details

5. **Assessment Management**
   - Add and delete assessments
   - View assessment details

6. **Grade Management**
   - Add and delete grades
   - View grade details

7. **Data Backup**
   - Backup deleted records for courses, instructors, students, enrollments, assessments, and grades

## Technologies Used

- Python
- Tkinter (for GUI)
- MySQL (for database)

## Setup Instructions

### Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)
- MySQL Server

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/prnsh03/eduschema-management-system.git

2. Install required Python packages:
   ```sh
   pip install mysql-connector-python

3. Set up the MySQL database:
* Create a database named EduSchema
* Create the required tables by running the SQL script provided in the database_setup.sql file

4. Update the database connection settings in the Python script:
   ```python
   DB_HOST = '127.0.0.1'
   DB_USER = 'root'
   DB_PASSWORD = 'yourpassword'
   DB_NAME = 'EduSchema'

5. Run the application:
   ``` sh
   python eduschema_management_system.py

Usage
* Course Management: Navigate to the 'Courses' tab to add, delete, and view courses.
* Instructor Management: Navigate to the 'Instructors' tab to add, delete, and view instructors.
* Student Management: Navigate to the 'Students' tab to add, delete, and view students.
* Enrollment Management: Navigate to the 'Enrollments' tab to add, delete, and view enrollments.
* Assessment Management: Navigate to the 'Assessments' tab to add, delete, and view assessments.
* Grade Management: Navigate to the 'Grades' tab to add, delete, and view grades.

