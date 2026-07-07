
#se puso max 3 para que sea mas facil de hacer las pruebas 
cursos = [
    {"id": 1, "nombre": "Python Básico", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
    {"id": 2, "nombre": "Excel Avanzado", "cupo_max": 2, "inscriptos": [], "lista_espera": []},
    {"id": 3, "nombre": "Diseño Web", "cupo_max": 3, "inscriptos": [], "lista_espera": []},
]

#funcion mostrar menu 
def mostrar_menu():
    """
    Muestra por pantalla las opciones disponibles del sistema de inscripción.

    No recibe parámetros ni devuelve ningún valor, solo imprime el menú
    para que el usuario elija una opción en el bucle principal.
    """

    print("\n--- Menu Sistema de Inscripción ---")
    print("ingrese numero corresondiente a la opcion que desea realizar")
    print("1. Inscribir estudiante")
    print("2. Ver cursos y cupos")
    print("3. Ver estadísticas")
    print("0. Salir")

#funcion mostrar cursos 
def ver_cursos(cursos):

    """
    Muestra por pantalla el listado de cursos con su información actual.

    Para cada curso imprime: ID, nombre, cantidad de inscriptos sobre el
    cupo máximo, cupos disponibles y cantidad de estudiantes en lista de espera.

    Args:
        cursos (list[dict]): Lista de cursos del sistema. Cada curso es un
            diccionario con las claves "id", "nombre", "cupo_max",
            "inscriptos" y "lista_espera".

    Returns:
        None
    """
    print("\n--- Cursos disponibles ---")
    for curso in cursos:
        inscriptos_actual = len(curso["inscriptos"])
        cupo_disponible = curso["cupo_max"] - inscriptos_actual
        en_espera = len(curso["lista_espera"])
        print(f"ID: {curso['id']} | {curso['nombre']} | Inscriptos: {inscriptos_actual}/{curso['cupo_max']} | Cupos disponibles: {cupo_disponible} | En lista de espera: {en_espera}")

#funcion inscribir estudiantes 
def inscribir_estudiante(cursos):
    
    """
    Inscribe a un estudiante en el curso seleccionado por ID.

    Solicita al usuario el ID del curso, el nombre del estudiante y su DNI,
    validando que los datos sean correctos (nombre no vacío, DNI numérico).
    Si el curso tiene cupo disponible, inscribe al estudiante; si está
    lleno, lo agrega a la lista de espera. Evita que un mismo DNI se
    inscriba dos veces en el mismo curso.

    Args:
        cursos (list[dict]): Lista de cursos del sistema, la cual se
            modifica in-place agregando el estudiante a "inscriptos" o
            "lista_espera" del curso correspondiente.

    Returns:
        None
    """
    ver_cursos(cursos)
    
    # Repetir hasta que el ID sea válido (numérico Y que exista un curso con ese ID)
    curso_seleccionado = None
    while curso_seleccionado is None:
        try:
            id_curso = int(input("Ingrese el ID del curso: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        for curso in cursos:
            if curso["id"] == id_curso:
                curso_seleccionado = curso
                break

        if curso_seleccionado is None:
            print("No existe un curso con ese ID. Intente nuevamente.")

    nombre_estudiante = input("Nombre del estudiante: ")
    while nombre_estudiante.strip() == "":
        print("El nombre no puede estar vacío.")
        nombre_estudiante = input("Nombre del estudiante: ")

    dni_valido = False
    while not dni_valido:
        try:
            dni_estudiante = int(input("DNI del estudiante: "))
            dni_valido = True
        except ValueError:
            print("El DNI debe ser un número válido. Intente nuevamente.")

    ya_inscripto = any(estudiante["dni"] == dni_estudiante for estudiante in curso_seleccionado["inscriptos"])
    ya_en_espera = any(estudiante["dni"] == dni_estudiante for estudiante in curso_seleccionado["lista_espera"])

    if ya_inscripto or ya_en_espera:
        print(f"El DNI {dni_estudiante} ya está registrado en el curso {curso_seleccionado['nombre']}.")
        return

    if len(curso_seleccionado["inscriptos"]) < curso_seleccionado["cupo_max"]:
        curso_seleccionado["inscriptos"].append({"nombre": nombre_estudiante, "dni": dni_estudiante})
        print(f"{nombre_estudiante} inscripto en {curso_seleccionado['nombre']}")
    else:
        curso_seleccionado["lista_espera"].append({"nombre": nombre_estudiante, "dni": dni_estudiante})
        print(f"El curso {curso_seleccionado['nombre']} está lleno. {nombre_estudiante} fue agregado a la lista de espera.")

#funcion ver estadisticas 
def ver_estadisticas(cursos):

    """
    Calcula y muestra las estadísticas generales del sistema.

    Incluye: total de estudiantes inscriptos (general y por curso), total
    de estudiantes en lista de espera (general y por curso), y el curso
    con mayor demanda, entendida como la suma de inscriptos más lista de
    espera de ese curso.

    Args:
        cursos (list[dict]): Lista de cursos del sistema sobre la cual se
            calculan los totales. No se modifica.

    Returns:
        None
    """
    print("\n--- Estadísticas ---")
    
    total_inscriptos = 0
    total_espera = 0
    curso_mas_demanda = None
    max_demanda = -1

    for curso in cursos:
        cantidad = len(curso["inscriptos"])
        espera = len(curso["lista_espera"])
        demanda = cantidad + espera
        
        total_inscriptos += cantidad
        total_espera += espera

        if demanda > max_demanda:
            max_demanda = demanda
            curso_mas_demanda = curso["nombre"]

    # 1) Estadísticas de inscriptos
    print("\n> Estadísticas de inscriptos:")
    print(f"Total de estudiantes inscriptos en el sistema: {total_inscriptos}")
    for curso in cursos:
        print(f"  - {curso['nombre']}: {len(curso['inscriptos'])} inscriptos")

    # 2) Control de listas de espera
    print("\n> Control de listas de espera:")
    print(f"Total de estudiantes en espera: {total_espera}")
    for curso in cursos:
        if len(curso["lista_espera"]) > 0:
            print(f"  - {curso['nombre']}: {len(curso['lista_espera'])} en espera")
    if total_espera == 0:
        print("  (No hay estudiantes en lista de espera)")

    # 3) Curso con mayor demanda (inscriptos + lista de espera)
    print("\n> Curso con mayor demanda:")
    print(f"{curso_mas_demanda} con {max_demanda} personas interesadas (inscriptos + lista de espera)")

#como una buena practica, se pone la funcion main para que el programa se ejecute desde ahi y no desde el codigo principal, esto permite que si se importa este archivo en otro, no se ejecute automaticamente
def main():
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
        elif opcion == "3":
            ver_estadisticas(cursos)
        else:
            print("opcion invalida, por favor ingrese un numero del 0 al 3")


#************************************************************************
#rama de ejecucion del programa

if __name__ == "__main__":
    main()