from gestion_sistema import GestionSistema
from estudiante import Estudiante
from curso import Curso

def menu():
    print("\n--- Sistema de Gestión de Estudiantes y Cursos ---")
    print("1. Registrar Estudiante")
    print("2. Registrar Curso")
    print("3. Inscribir Estudiante en Curso")
    print("4. Listar Cursos de un Estudiante")
    print("5. Eliminar Inscripción")
    print("0. Salir")
    return input("Seleccione una opción: ")

if __name__ == "__main__":
    sistema = GestionSistema()

    while True:
        opcion = menu()
        if opcion == '1':
            identificador = input("Identificador del estudiante: ")
            nombre = input("Nombre completo del estudiante: ")
            correo = input("Correo electrónico del estudiante: ")
            estudiante = Estudiante(identificador, nombre, correo)
            sistema.registrar_estudiante(estudiante)
        elif opcion == '2':
            identificador = input("Identificador del curso: ")
            nombre = input("Nombre del curso: ")
            descripcion = input("Descripción del curso: ")
            creditos = int(input("Cantidad de créditos del curso: "))
            curso = Curso(identificador, nombre, descripcion, creditos)
            sistema.registrar_curso(curso)
        elif opcion == '3':
            estudiante_id = input("Identificador del estudiante a inscribir: ")
            curso_id = input("Identificador del curso a inscribir: ")
            sistema.inscribir_estudiante_en_curso(estudiante_id, curso_id)
        elif opcion == '4':
            estudiante_id = input("Identificador del estudiante para listar sus cursos: ")
            sistema.listar_cursos_de_estudiante(estudiante_id)
        elif opcion == '5':
            estudiante_id = input("Identificador del estudiante para eliminar la inscripción: ")
            curso_id = input("Identificador del curso para eliminar la inscripción: ")
            sistema.eliminar_inscripcion(estudiante_id, curso_id)
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
