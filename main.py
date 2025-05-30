

from funciones import (
    cargar_participantes, 
    cargar_puntuaciones, 
    mostrar_puntajes,
    mostrar_promedios_menores_a_4,
    mostrar_promedios_menores_a_8,
    promedio_por_jurado,
    jurado_mas_estricto,
    mostrar_ordenados_por_promedio,
    mostrar_ganador,
    exportar_a_txt,
    mostrar_top3,
    mostrar_ordenados_alfabeticamente
)

participantes = []
datos_cargados = False

while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cargar participantes")
        print("2. Cargar puntuaciones")
        print("3. Mostrar puntajes y promedios")
        print("4. Mostrar participantes con promedio menor a 4")
        print("5. Mostrar participantes con promedio menor a 8")
        print("6. Promedio por jurado")
        print("7. Jurado más estricto")
        print("8. Mostrar participantes ordenados por promedio")
        print("9. Mostrar ganador")
        print("10. Exportar a archivo de texto")
        print("11. Mostrar 3 participantes con mayor puntaje")
        print("12. Mostrar participantes ordenados alfabéticamente")
        print("0. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            participantes = cargar_participantes()
            datos_cargados = True
        elif opcion == "2":
            if not datos_cargados:
                print("Primero debés cargar los participantes.")
            else:
                cargar_puntuaciones(participantes)
        elif opcion == "3":
            if not datos_cargados:
                print("Primero debés cargar los participantes y puntajes.")
            elif participantes[0]["j1"] is None:
                print("Primero debés cargar las puntuaciones.")
            else:
                mostrar_puntajes(participantes)
        elif opcion == "4":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                mostrar_promedios_menores_a_4(participantes)
        elif opcion == "5":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                mostrar_promedios_menores_a_8(participantes)
        elif opcion == "6":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                promedio_por_jurado(participantes)
        elif opcion == "7":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                jurado_mas_estricto(participantes)
        elif opcion == "8":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                mostrar_ordenados_por_promedio(participantes)
        elif opcion == "9":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                mostrar_ganador(participantes)
        elif opcion == "10":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                exportar_a_txt(participantes)
        elif opcion == "11":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                mostrar_top3(participantes)
        elif opcion == "12":
            if not datos_cargados or participantes[0]["j1"] is None:
                print("Primero debés cargar los participantes y las puntuaciones.")
            else:
                mostrar_ordenados_alfabeticamente(participantes)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intentá de nuevo.")


