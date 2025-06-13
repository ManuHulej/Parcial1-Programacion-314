from funciones import (
    cargar_participantes,
    cargar_puntuaciones,
    mostrar_puntajes,
    mostrar_promedios_menores_a_4,
    mostrar_promedios_menores_a_8,
    promedio_por_jurado,
    jurado_mas_estricto,
    jurado_mas_generoso,
    mostrar_puntajes_iguales,
    buscar_participante_por_nombre,
    mostrar_top3,
    mostrar_ordenados_alfabeticamente,
    mostrar_ganador,
    resolver_empate
)

participantes = []
datos_cargados = False
puntajes_cargados = False
CANTIDAD_PARTICIPANTES = 5

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntajes y promedios")
    print("4. Mostrar participantes con promedio menor a 4")
    print("5. Mostrar participantes con promedio menor a 8")
    print("6. Promedio por jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Mostrar 3 participantes con mayor puntaje")
    print("12. Mostrar participantes ordenados alfabéticamente")
    print("13. Mostrar ganador o empate")
    print("14. Realizar desempate (si corresponde)")
    print("0. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        participantes = cargar_participantes(CANTIDAD_PARTICIPANTES)
        datos_cargados = True

    elif opcion == "2":
        if not datos_cargados:
            print("Primero debés cargar los participantes.")
        else:
            puntajes_cargados = cargar_puntuaciones(participantes)

    elif opcion == "3":
        if datos_cargados and puntajes_cargados:
            mostrar_puntajes(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "4":
        if datos_cargados and puntajes_cargados:
            mostrar_promedios_menores_a_4(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "5":
        if datos_cargados and puntajes_cargados:
            mostrar_promedios_menores_a_8(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "6":
        if datos_cargados and puntajes_cargados:
            promedio_por_jurado(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "7":
        if datos_cargados and puntajes_cargados:
            jurado_mas_estricto(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "8":
        if datos_cargados and puntajes_cargados:
            jurado_mas_generoso(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "9":
        if datos_cargados and puntajes_cargados:
            mostrar_puntajes_iguales(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "10":
        if datos_cargados and puntajes_cargados:
            buscar_participante_por_nombre(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "11":
        if datos_cargados and puntajes_cargados:
            mostrar_top3(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "12":
        if datos_cargados and puntajes_cargados:
            mostrar_ordenados_alfabeticamente(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "13":
        if datos_cargados and puntajes_cargados:
            ganadores = mostrar_ganador(participantes)
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "14":
        if datos_cargados and puntajes_cargados:
            ganadores = mostrar_ganador(participantes)
            if len(ganadores) > 1:
                resolver_empate(ganadores)
            else:
                print("No hay empate. Ya hay un único ganador.")
        else:
            print("Primero debés cargar los participantes y las puntuaciones.")

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intentá de nuevo.")
