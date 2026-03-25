students = {}

while True:
    print("\n1 - add student")
    print("2 - show students")
    print("3 - show average")
    print("4 - best student")
    print("5 - quit program")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter student's name: ")
        grade = float(input("Enter student's grade: "))

        students[name] = grade
        print("Student added!")

    elif choice == '2':
        if not students:
            print("No students yet.")
        else:
            for name, grade in students.items():
                print(name, "->", grade)

    elif choice == '3':
        if not students:
            print("No students yet.")
        else:
            avg = sum(students.values()) / len(students)
            print("Average grade:", avg)

    elif choice == '4':
        if not students:
            print("No students yet.")
        else:
            best = max(students, key=students.get)
            print("Best student:", best, "(", students[best], ")")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")