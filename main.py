
#se puso max 3 para que sea mas facil de hacer las pruebas 
cursos = [
    {"nombre": "Python Básico", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
    {"nombre": "Excel Avanzado", "cupo_max": 2, "inscriptos": [], "lista_espera": []},
    {"nombre": "Diseño Web", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
]

#funcion mostrar menu 
def mostrar_menu():

    print("\n--- Sistema de Inscripción ---")
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
        print(f"{curso['nombre']} | Inscriptos: {inscriptos_actual}/{curso['cupo_max']} | Cupos disponibles: {cupo_disponible}")

#funcion inscribir estudiantes (el nombre tiene escribirse tal y como esta o no lo tomara)
def inscribir_estudiante(cursos):
    ver_cursos(cursos)
    nombre_curso = input("¿A qué curso desea inscribirse? ")
    nombre_estudiante = input("Nombre del estudiante: ")
    
    for curso in cursos:
        if curso["nombre"] == nombre_curso:
            curso["inscriptos"].append({"nombre": nombre_estudiante})
            print(f"{nombre_estudiante} inscripto en {nombre_curso}")
            return
    print("Curso no encontrado")

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
