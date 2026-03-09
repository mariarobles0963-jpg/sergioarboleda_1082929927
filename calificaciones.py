#sistema de registro de estudiantes

estudiantes = []

for i in range(5):
    while True:
        nombre = input(f"nombre del estudiante {i + 1}: ")
        try: 
            edad = int(input(f"edad"))
            calificaciones = float(input(f"calificacion"))
            if 5 <=edad <=100 and 0 <= calificaciones <= 5:
                estudiantes.append({"nombre": nombre, "edad": edad, "calificaciones": calificaciones})
                break
            else:
                print("datos invalidos, la edad debe estar entre 5 y 100, y las calificaciones entre 0 y 5.")
        except ValueError:
            print("entrada invalida, por favor ingrese un numero para la edad y las calificaciones.")

#calcular estadisticas
if estudiantes:
    estudiantes_max = max(estudiantes, key=lambda e: e["calificaciones"]) 
    estudiantes_min = min(estudiantes, key=lambda e: e["calificaciones"])
    promedio_calificaciones = sum(e["calificaciones"] for e in estudiantes) / len(estudiantes)
    
    print("estudiante con la calificacion mas alta:")
    print(f"nombre: {estudiantes_max['nombre']}, edad: {estudiantes_max['edad']}, calificaciones: {estudiantes_max['calificaciones']}") 

    print("\nEstudiante con la calificacion mas baja:")
    print(f"nombre: {estudiantes_min['nombre']}, edad: {estudiantes_min['edad']}, calificaciones: {estudiantes_min['calificaciones']}")

    print(f"\nCalificacion promedio de todos: {promedio_calificaciones:.2f}")