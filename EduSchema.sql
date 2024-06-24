CREATE DATABASE IF NOT EXISTS EduSchema;
USE EduSchema;


CREATE TABLE IF NOT EXISTS Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    assessment_name VARCHAR(255) NOT NULL,
    due_date DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE IF NOT EXISTS Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    assessment_id INT NOT NULL,
    grade FLOAT NOT NULL,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id)
);

SELECT * FROM Courses;

INSERT INTO Courses (course_name, course_description, start_date, end_date) VALUES
('Introduction to Python', 'Learn the basics of Python programming.', '2024-01-01', '2024-03-01'),
('Advanced Java', 'Deep dive into advanced Java topics.', '2024-02-15', '2024-05-15'),
('Database Management', 'Introduction to relational databases and SQL.', '2024-03-01', '2024-06-01');

INSERT INTO Instructors (first_name, last_name, email, phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '234-567-8901'),
('Emily', 'Johnson', 'emily.johnson@example.com', '345-678-9012');

INSERT INTO Students (first_name, last_name, email, phone) VALUES
('Alice', 'Brown', 'alice.brown@example.com', '456-789-0123'),
('Bob', 'Davis', 'bob.davis@example.com', '567-890-1234'),
('Charlie', 'Evans', 'charlie.evans@example.com', '678-901-2345');

INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2024-01-01'),
(2, 1, '2024-01-02'),
(3, 2, '2024-02-15'),
(1, 3, '2024-03-01'),
(2, 3, '2024-03-01');

INSERT INTO Assessments (course_id, assessment_name, due_date)
VALUES 
    (1, 'Python Basics Quiz', '2024-01-15'),
    (1, 'Midterm Project', '2024-02-01'),
    (2, 'Java Assignment 1', '2024-03-01'),
    (3, 'SQL Quiz', '2024-03-15');

INSERT INTO Grades (enrollment_id, assessment_id, grade) VALUES
(1, 1, 95.0),
(1, 2, 88.5),
(2, 1, 78.0),
(3, 3, 90.0),
(4, 4, 85.5);


CREATE TABLE eduschema.backup_courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255),
    course_description TEXT,
    start_date DATE,
    end_date DATE,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eduschema.backup_students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE eduschema.backup_instructors (
	instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eduschema.backup_grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    assessment_id INT NOT NULL,
    grade FLOAT NOT NULL,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eduschema.backup_assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    assessment_name VARCHAR(255) NOT NULL,
    due_date DATE NOT NULL,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eduschema.backup_enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
