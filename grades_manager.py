def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}
def add_student(student_grades={}):
    name = input("Enter student name: ").title()
    subjects = {}
    while True:
        mensajeentrada = input("Enter subject and grade (or 'exit' to finish): ").lower()
        if mensajeentrada == "exit":
            break
        materia_nota = mensajeentrada.split(",")
        subject = materia_nota[0].title()
        grade = float(materia_nota[1])
        subjects[subject] = grade
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades
def get_students(student_grades, keys):
    diccionario = {}
    for name in keys:
        estudiante = False
        for student in student_grades:
            if student.lower() == name.lower():
                diccionario[student.title()] = student_grades[student]
                estudiante = True
        if estudiante == False:
            print(name.title() + " not found!")
    return diccionario