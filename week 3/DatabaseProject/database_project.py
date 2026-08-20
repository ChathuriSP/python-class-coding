import sqlite3

def create_connection():
    conn = sqlite3.connect("university.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            F_name TEXT NOT NULL,
            L_name TEXT NOT NULL,
            NID TEXT NOT NULL,
            B_date DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer (
            lecture_id INTEGER PRIMARY KEY AUTOINCREMENT,
            L_firstname TEXT NOT NULL,
            L_lastname TEXT NOT NULL,
            L_address TEXT NOT NULL,
            L_email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_code TEXT NOT NULL,
            lecture_id INTEGER NOT NULL,
            course_unit TEXT NOT NULL,
            FOREIGN KEY (lecture_id) REFERENCES lecturer (lecture_id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrolments (
            enrolment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id  INTEGER,
            course_id INTEGER,
            date_of_enrolment DATE NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    ''')
    conn.commit()
    conn.close()
    print("All tables created successfully!")

def insert_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        #insert 5 students
        
        
    ''')


create_table()