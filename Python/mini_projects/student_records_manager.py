"""
Student Record Manager
A simple CLI program to manage student records using Python.
Covers dictionaries, functions, loops, and basic validation.
"""

students = {}

def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("Student already exists.")
        return
    name = input("Enter name: ").strip()
    marks = float(input("Enter marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")

def view_students():
    if not students:
        print("No records found.")
        return
    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

def main():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
