from database_project import create_connection

# Add 5 Students

def add_student(F_name, L_name, NID, B_date):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO students (F_name, L_name, NID, B_date)
            VALUES (?, ?, ?, ?)
        """, (F_name, L_name, NID, B_date))

        conn.commit()
        print("Student added successfully.")

    except Exception as e:
        print("Error adding student:", e)

    finally:
        conn.close()


def add_sample_students():
    conn = create_connection()
    cursor = conn.cursor()

    students = [
        ("Chathuri", "Perera", "N001", "1988-05-15"),
        ("Vikum", "Fernando", "N002", "1988-06-25"),
        ("Sayuni", "Perera", "N003", "1988-01-15"),
        ("Tharushi", "Kumari", "N004", "1988-02-13"),
        ("Ravindu", "Silva", "N005", "1988-10-17")
    ]

    try:
        cursor.executemany("""
            INSERT INTO students (F_name, L_name, NID, B_date)
            VALUES (?, ?, ?, ?)
        """, students)

        conn.commit()
        print("5 students added successfully.")

    except Exception as e:
        print("Error adding students:", e)

    finally:
        conn.close()

# Add 2 Lecturers


def add_lecturer(L_lastname, L_firstname, L_address, L_email):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO lecturer
            (L_firstname, L_lastname, L_address, L_email) 
            VALUES (?, ?, ?, ?)
        """, (L_firstname, L_lastname, L_address, L_email))

        conn.commit()
        print("Lecturer added successfully.")

    except Exception as e:
        print("Error adding lecturer:", e)

    finally:
        conn.close()


def add_sample_lecturers():
    conn = create_connection()
    cursor = conn.cursor()

    lecturers = [
        ("Chathura", "Rajapaksha", "Auckland", "chathura@gmail.com"),
        ("Madushanka", "Jayasuriya", "Wellington", "madu123@gmail.com")
    ]

    try:
        cursor.executemany("""
            INSERT INTO lecturer
            (L_firstname, L_lastname, L_address, L_email)
            VALUES (?, ?, ?, ?)
        """, lecturers)

        conn.commit()
        print("2 lecturers added successfully.")

    except Exception as e:
        print("Error adding lecturers:", e)

    finally:
        conn.close()

# Add 3 Courses

def add_course(course_name, course_code, lecture_id, course_unit):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO courses
            (course_name, course_code, lecture_id, course_unit)
            VALUES (?, ?, ?, ?)
        """, (course_name, course_code, lecture_id, course_unit))

        conn.commit()
        print("Course added successfully.")

    except Exception as e:
        print("Error adding course:", e)

    finally:
        conn.close()


def add_sample_courses():
    conn = create_connection()
    cursor = conn.cursor()

    courses = [
        ("Software Engineering", "CC001", 1, "IT"),
        ("Business Informatics", "CC002", 2, "Management"),
        ("Business Management", "CC003", 2, "Management")
    ]

    try:
        cursor.executemany("""
            INSERT INTO courses
            (course_name, course_code, lecture_id, course_unit)
            VALUES (?, ?, ?, ?)
        """, courses)

        conn.commit()
        print("3 courses added successfully.")

    except Exception as e:
        print("Error adding courses:", e)

    finally:
        conn.close()

# Add Enrolment Records

def add_sample_enrolments():
    conn = create_connection()
    cursor = conn.cursor()

    enrolments = [
        (1, 1, "2026-08-01"),
        (1, 2, "2026-08-01"),
        (2, 1, "2026-08-02"),
        (2, 3, "2026-08-02"),
        (3, 2, "2026-08-03"),
        (3, 3, "2026-08-03"),
        (4, 1, "2026-08-04"),
        (4, 2, "2026-08-04"),
        (5, 2, "2026-08-05"),
    ]

    try:
        cursor.executemany("""
            INSERT INTO enrolments
            (student_id, course_id, date_of_enrolment)
            VALUES (?, ?, ?)
        """, enrolments)

        conn.commit()
        print("Enrolment records added successfully.")

    except Exception as e:
        print("Error adding enrolments:", e)

    finally:
        conn.close()

# View Students

def view_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return rows

# View Courses

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()

    conn.close()

    return rows
# View Lecturers

def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lecturer")
    rows = cursor.fetchall()

    conn.close()

    return rows


# View Enrolments

def view_enrolments():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM enrolments")
    rows = cursor.fetchall()

    conn.close()

    return rows

# Q1 - How many students are registered in each course
def students_per_course():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            courses.course_name,
            COUNT(enrolments.student_id) AS student_count
        FROM courses
        LEFT JOIN enrolments
            ON courses.course_id = enrolments.course_id
        GROUP BY courses.course_id, courses.course_name
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# Q2 - List the names and student IDs of students who have enrolled in more than one course.
def students_more_than_one_course():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            students.student_id,
            students.F_name,
            students.L_name,
            COUNT(enrolments.course_id) AS course_count
        FROM students
        JOIN enrolments
            ON students.student_id = enrolments.student_id
        GROUP BY students.student_id, students.F_name, students.L_name
        HAVING COUNT(enrolments.course_id) > 1
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows