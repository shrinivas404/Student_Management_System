students = []

def view_students():
    if not students:
        print("No students available.")
        return

    print("\nStudent List")
    print("-" * 30)

    for student in students:
        print(f"Roll No: {student['roll']}")
        print(f"Name: {student['name']}")
        print(f"Department: {student['department']}")
        print("-" * 30)


def search_student(roll_no):
    for student in students:
        if student["roll"] == roll_no:
            print("\nStudent Found")
            print(f"Roll No: {student['roll']}")
            print(f"Name: {student['name']}")
            print(f"Department: {student['department']}")
            return

    print("Student not found.")