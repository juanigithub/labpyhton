
#se puso max 3 para que sea mas facil de hacer las pruebas 
cursos = [
    {"id": 1, "nombre": "Python Básico", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
    {"id": 2, "nombre": "Excel Avanzado", "cupo_max": 2, "inscriptos": [], "lista_espera": []},
    {"id": 3, "nombre": "Diseño Web", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
]

#funcion mostrar menu 
def mostrar_menu():

    print("\n--- Menu Sistema de Inscripción ---")
    print("ingrese numero corresondiente a la opcion que desea realizar")
    print("1. Inscribir estudiante")
    print("2. Ver cursos y cupos")
    print("3. Ver estadísticas")
    print("0. Salir")

#funcion mostrar cursos 
def ver_cursos(cursos):
    print("\n--- Cursos disponibles ---")
    for curso in cursos:
        inscriptos_actual = len(curso["inscriptos"])
        cupo_disponible = curso["cupo_max"] - inscriptos_actual
        en_espera = len(curso["lista_espera"])
        print(f"ID: {curso['id']} | {curso['nombre']} | Inscriptos: {inscriptos_actual}/{curso['cupo_max']} | Cupos disponibles: {cupo_disponible} | En lista de espera: {en_espera}")

#funcion inscribir estudiantes (el nombre tiene escribirse tal y como esta o no lo tomara)
def inscribir_estudiante(cursos):
    ver_cursos(cursos)
    try:
        id_curso = int(input("Ingrese el ID del curso: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    nombre_estudiante = input("Nombre del estudiante: ")
    while nombre_estudiante.strip() == "":
        print("El nombre no puede estar vacío.")
        nombre_estudiante = input("Nombre del estudiante: ")

    for curso in cursos:
        if curso["id"] == id_curso:
            if len(curso["inscriptos"]) < curso["cupo_max"]:
                curso["inscriptos"].append({"nombre": nombre_estudiante})
                print(f"{nombre_estudiante} inscripto en {curso['nombre']}")
            else:
                curso["lista_espera"].append({"nombre": nombre_estudiante})
                print(f"El curso {curso['nombre']} está lleno. {nombre_estudiante} fue agregado a la lista de espera.")
            return
    print("No existe un curso con ese ID.")

#rama de ejecucion del programa
while True:
    mostrar_menu()
    opcion = input("seleccione una opción: ")
    if opcion == "0":
        print("¡Hasta luego!")
        break 
    elif opcion == "1":
        inscribir_estudiante(cursos)
    elif opcion == "2":
        ver_cursos(cursos)  
    else:
        print("Función aún no implementada")
