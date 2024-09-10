# Variables globales
estudiantes = []
cursos = ["Matemáticas", "Física", "Química", "Historia", "Literatura"]

# Función para mostrar el menú principal
def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Registrar Estudiante")
    print("2. Ver Cursos Disponibles")
    print("3. Matricularse en un Curso")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

# Función para registrar un estudiante
def registrar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ").strip()
    if nombre:
        estudiantes.append(nombre)
        print(f"Estudiante {nombre} registrado con éxito.")
    else:
        print("El nombre no puede estar vacío.")

# Función para ver los cursos disponibles
def ver_cursos():
    print("\n--- Cursos Disponibles ---")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso}")

# Función para matricularse en un curso
def matricular_curso():
    if not estudiantes:
        print("No hay estudiantes registrados. Registra un estudiante primero.")
        return
    
    print("\n--- Estudiantes Registrados ---")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"{i}. {estudiante}")
    
    estudiante_idx = input("Selecciona el número del estudiante: ")
    try:
        estudiante_idx = int(estudiante_idx) - 1
        if 0 <= estudiante_idx < len(estudiantes):
            ver_cursos()
            curso_idx = input("Selecciona el número del curso: ")
            try:
                curso_idx = int(curso_idx) - 1
                if 0 <= curso_idx < len(cursos):
                    print(f"{estudiantes[estudiante_idx]} se ha matriculado en {cursos[curso_idx]}.")
                else:
                    print("Selección de curso no válida.")
            except ValueError:
                print("Entrada no válida para el curso.")
        else:
            print("Selección de estudiante no válida.")
    except ValueError:
        print("Entrada no válida para el estudiante.")

# Función principal que integra todo el sistema
def main():
    while True:
        opcion = menu_principal()
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            ver_cursos()
        elif opcion == '3':
            matricular_curso()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
