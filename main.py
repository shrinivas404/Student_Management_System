from student import (
    add_student,
    delete_student,
    view_students,
    search_student
)

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")
        search_student(roll_no)

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Please try again.")