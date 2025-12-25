"""
Student Grade Analyzer
Mini CLI project for managing students and analyzing grades.
Concepts: dictionaries, lists, functions, loops, conditions.
"""

students = {}

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter name: ").strip()
    marks = []

    for i in range(3):
        score = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(score)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    students[roll] = {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    print("Student added successfully.")

def view_students():
    if not students:
        print("No records found.")
        return

    for roll, data in students.items():
        print("-" * 40)
        print(f"Roll   : {roll}")
        print(f"Name   : {data['name']}")
        print(f"Marks  : {data['marks']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade  : {data['grade']}")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

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
