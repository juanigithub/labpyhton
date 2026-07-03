
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



while True:
    mostrar_menu()
    opcion = input ("seleccione una opción: ")
    if opcion == "0":
        print("¡Hasta luego!")
        break   
    else:
        print("Función aún no implementada")
