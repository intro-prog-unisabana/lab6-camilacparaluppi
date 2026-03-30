from grades_manager import add_student, avg_by_student
print("Welcome to the Student Grades Manager!")
my_grades = {}
while True:
    option = input("\nSelect an option:\n1. Add a student\n2. Print student grade averages\n3. Exit\n")
    if option == "1":
        my_grades = add_student(my_grades)
    elif option == "2":
        suboption = input("\nSelect an option:\na. Display all students\nb. Display selected students\n")
        if suboption == "a":
            avg_by_student(my_grades)
        elif suboption == "b":
            names = input("Enter student names (comma-separated): ")
            keys = names.split(",")
            clean_keys = []
            for name in keys:
                clean_keys.append(name.strip())
            avg_by_student(my_grades, clean_keys)
        else:
            print("Invalid option selected!")
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected!")