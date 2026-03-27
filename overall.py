def student_averages(students):
    result = {}
    for student, notas in students.items():
        suma = 0
        cantidad = 0
        for tarea, nota in notas.items():
            suma = suma + nota
            cantidad = cantidad + 1
        promedio = round(suma / cantidad)
        result[student] = promedio
    return result
def assignment_averages(students):
    result = {}
    for student, notas in students.items():
        for tarea, nota in notas.items():
            if tarea in result:
                result[tarea] = result[tarea] + nota
            else:
                result[tarea] = nota
    for tarea in result:
        result[tarea] = round(result[tarea] / len(students))
    return result