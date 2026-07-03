
#se puso max 3 para que sea mas facil de hacer las pruebas 
cursos = [
    {"nombre": "Python Basico", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
    {"nombre": "Excel Avanzado", "cupo_max": 2, "inscriptos": [], "lista_espera": []},
    {"nombre": "Diseño Web", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
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
        print(f"{curso['nombre']} | Inscriptos: {inscriptos_actual}/{curso['cupo_max']} | Cupos disponibles: {cupo_disponible} | En lista de espera: {en_espera}")

#funcion inscribir estudiantes (el nombre tiene escribirse tal y como esta o no lo tomara)
def inscribir_estudiante(cursos):
    ver_cursos(cursos)
    nombre_curso = input("¿A qué curso desea inscribirse? ")
    nombre_estudiante = input("Nombre del estudiante: ")
    #validacion de que el nombre no este vacio strip rechaza el caso en que el usuario ponga solo espacios en blanco (" ") como si fuera un nombre.
    while nombre_estudiante.strip() == "":
        print("El nombre no puede estar vacío.")
        nombre_estudiante = input("Nombre del estudiante: ")
    
    for curso in cursos:
        #lower normaliza ambos lados en minusculas para que no haya problemas al comparar.
        if curso["nombre"].lower() == nombre_curso.lower():
            #mientras haya menos inscriptos que el cupo máximo, entra en el curso normal.
            if len(curso["inscriptos"]) < curso["cupo_max"]:
                curso["inscriptos"].append({"nombre": nombre_estudiante})
                print(f"{nombre_estudiante} inscripto en {curso['nombre']}")
            else:
                curso["lista_espera"].append({"nombre": nombre_estudiante})
                print(f"El curso {curso['nombre']} está lleno. {nombre_estudiante} fue agregado a la lista de espera.")
            return
    print("Curso no encontrado")

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
