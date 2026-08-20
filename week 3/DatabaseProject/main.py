from database_project import create_table
from user_manager import (
    add_sample_students,
    add_sample_lecturers,
    add_sample_courses,
    add_sample_enrolments,
    view_students,
    view_lecturers,
    view_courses,
    view_enrolments,
    students_per_course,
    students_more_than_one_course
)


# Create database tables
create_table()

# Insert sample data
add_sample_students()
add_sample_lecturers()
add_sample_courses()
add_sample_enrolments()

# Display Students
print("\n--- Students ---")
for row in view_students():
    print(row)


# Display Lecturers
print("\n--- Lecturers ---")
for row in view_lecturers():
    print(row)


# Display Courses
print("\n--- Courses ---")
for row in view_courses():
    print(row)


# Display Enrolments
print("\n--- Enrolments ---")
for row in view_enrolments():
    print(row)

print("\n--- Q.1: Students per courses ---")

for row in students_per_course():
    print(row)


print("\n--- Q.2: Students enrolled in more than one course---")

for row in students_more_than_one_course():
    print(row)
