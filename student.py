students = []

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "department": department
    }

    students.append(student)
    print("Student added successfully!")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")
def view_students():
    if not students:
        print("No students available.")
        return

    print("\nStudent List")
    print("-" * 30)

    for student in students:
        print(f"Roll No: {student['roll_no']}")
        print(f"Name: {student['name']}")
        print(f"Department: {student['department']}")
        print("-" * 30)


def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(f"Roll No: {student['roll_no']}")
            print(f"Name: {student['name']}")
            print(f"Department: {student['department']}")
            return

    print("Student not found.")