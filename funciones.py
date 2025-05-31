# Parcial de Programación - Funciones para gestionar participantes

from inputs import pedir_nombre, pedir_puntaje


# Funcion auxiliar para calcular el promedio de un participante
def calcular_promedio(p):
    """
    Calcula y devuelve el promedio de un participante redondeado a 2 decimales.
    """
    promedio = (p["j1"] + p["j2"] + p["j3"]) / 3
    return int(promedio * 100) / 100


def cargar_participantes():
    """
    Carga 5 participantes validando el nombre a través de la función pedir_nombre().
    
    """
    participantes = [None, None, None, None, None]
    i = 0
    while i < 5:
        nombre = pedir_nombre()
        participante = {
            "nombre": nombre,
            "j1": None,
            "j2": None,
            "j3": None
        }
        participantes[i] = participante
        i = i + 1
    return participantes


def cargar_puntuaciones(participantes):
    """
    Carga las puntuaciones de los tres jurados para cada participante.
    Usa la función pedir_puntaje() para validar los valores.
    """
    i = 0
    while i < len(participantes):
        participante = participantes[i]
        print("\nIngresá los puntajes para", participante["nombre"])
        participante["j1"] = pedir_puntaje("Jurado 1")
        participante["j2"] = pedir_puntaje("Jurado 2")
        participante["j3"] = pedir_puntaje("Jurado 3")
        i = i + 1

    print("Puntuaciones cargadas correctamente.")


def mostrar_puntajes(participantes):
    """
    Muestra el nombre y las notas de cada jurado junto con el promedio de cada participante.
    """
    
    print("\n--- PUNTAJES Y PROMEDIOS ---")
    for p in participantes:
        nombre = p["nombre"]
        j1 = p["j1"]
        j2 = p["j2"]
        j3 = p["j3"]
        promedio = calcular_promedio(p)

        print(f"\nParticipante: {nombre}")
        print(f"  Jurado 1: {j1}")
        print(f"  Jurado 2: {j2}")
        print(f"  Jurado 3: {j3}")
        print(f"  Promedio: {promedio:.2f}")

def mostrar_promedios_menores_a_4(participantes):
    """
    Muestra los participantes cuyo promedio es menor a 4.
    Si no hay ninguno, informa que no se encontraron.
    """
    
    encontrados = False 
    print("\n--- Participantes con promedio menor a 4 ---")
    
    for p in participantes:
        promedio = calcular_promedio(p)
        if promedio < 4:
            encontrados = True
            print(f"{p['nombre']} - Promedio: {promedio:.2f}")
    
    if not encontrados:
        print("No hay participantes con promedio menor a 4.")

def mostrar_promedios_menores_a_8(participantes):
    """
    Muestra los participantes cuyo promedio es menor a 8.
    Si no hay ninguno, informa que no se encontraron.
    """
    encontrados = False
    print("\n--- Participantes con promedio menor a 8 ---")
    
    for p in participantes:
        promedio = calcular_promedio(p)
        if promedio < 8:
            encontrados = True
            print(f"{p['nombre']} - Promedio: {promedio:.2f}")
    
    if not encontrados:
        print("No hay participantes con promedio menor a 8.")

def promedio_por_jurado(participantes):
    """
    Calcula y muestra el promedio general de cada jurado.
    """
    
    total_j1 = 0
    total_j2 = 0
    total_j3 = 0
    cantidad = 0

    i = 0
    while i < len(participantes):
        total_j1 = total_j1 + participantes[i]["j1"]
        total_j2 = total_j2 + participantes[i]["j2"]
        total_j3 = total_j3 + participantes[i]["j3"]
        
        cantidad +=  1
        i+=  1

    promedio_j1 = int((total_j1 / cantidad) * 100) / 100
    promedio_j2 = int((total_j2 / cantidad) * 100) / 100
    promedio_j3 = int((total_j3 / cantidad) * 100) / 100

    print("\n--- Promedio de cada jurado ---")
    print("Jurado 1:", promedio_j1)
    print("Jurado 2:", promedio_j2)
    print("Jurado 3:", promedio_j3)
    
    return promedio_j1, promedio_j2, promedio_j3

def jurado_mas_estricto(participantes):
    """
    Muestra todos los jurados que tengan el promedio más bajo.
    Usa la función promedio_por_jurado para obtener los promedios.
    """
    promedio_j1, promedio_j2, promedio_j3 = promedio_por_jurado(participantes)

    minimo = promedio_j1
    if promedio_j2 < minimo:
        minimo = promedio_j2
    if promedio_j3 < minimo:
        minimo = promedio_j3

    print("\n--- Jurado/s más estricto/s ---")
    if promedio_j1 == minimo:
        print("Jurado 1 con promedio de", promedio_j1)
    if promedio_j2 == minimo:
        print("Jurado 2 con promedio de", promedio_j2)
    if promedio_j3 == minimo:
        print("Jurado 3 con promedio de", promedio_j3)



def mostrar_ordenados_por_promedio(participantes):
    """
    Calcula el promedio de cada participante, los ordena de menor a mayor
    utilizando el algoritmo de ordenamiento burbuja, y los muestra por pantalla.

    """
    
    
    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = calcular_promedio(p)  
        p["promedio"] = promedio
        i += 1
        
    n = len(participantes)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if participantes[j]["promedio"] > participantes[j+1]["promedio"]:
                
                aux = participantes[j]
                participantes[j] = participantes[j+1]
                participantes[j+1] = aux
            j += 1
        i += 1

    print("\n--- Participantes ordenados por promedio ---")
    k = 0
    while k < len(participantes):
        p = participantes[k]
        print(p["nombre"], "- Promedio:", p["promedio"])
        k += 1

def mostrar_ganador(participantes):
    
    """
    Calcula el promedio de cada participante y muestra el que tenga el mayor promedio.
    
    """
    
    i = 0
    mejor_promedio = -1
    ganador = ""

    while i < len(participantes):
        p = participantes[i]
        promedio = calcular_promedio(p)

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            ganador = p["nombre"]

        i = i + 1

    print("\n--- GANADOR/A DEL CONCURSO ---")
    print("El ganador es", ganador, "con promedio de", mejor_promedio)

def exportar_a_txt(participantes):
    """
    Calcula el promedio de cada participante y exporta los datos a un archivo de texto (.txt).
    Cada línea del archivo contiene el nombre del participante y su promedio.
    
    """
    
    
    archivo = open("resultados.txt", "w")

    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = calcular_promedio(p)

        linea = p["nombre"] + " - Promedio: " + str(promedio) + "\n"
        archivo.write(linea)
        i = i + 1

    archivo.close()
    print("Archivo 'resultados.txt' exportado correctamente.")

def mostrar_top3(participantes):
    """
    Calcula el promedio de cada participante, los ordena de mayor a menor usando burbuja,
    y muestra en pantalla los tres con mejor promedio.

    """
    
    
    datos = [None] * len(participantes)

    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = (p["j1"] + p["j2"] + p["j3"]) / 3
        promedio = int(promedio * 100) / 100

        fila = [None] * 2
        fila[0] = p["nombre"]
        fila[1] = promedio
        datos[i] = fila
        i = i + 1

    n = len(datos)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if datos[j][1] < datos[j + 1][1]:
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux
            j = j + 1
        i = i + 1

    print("\n--- TOP 3 PROMEDIOS ---")
    k = 0
    while k < 3 and k < len(datos):
        print(datos[k][0], "- Promedio:", datos[k][1])
        k = k + 1

def mostrar_ordenados_alfabeticamente(participantes):
    """
    Calcula el promedio de cada participante, los ordena alfabéticamente por nombre
    usando el algoritmo de burbuja, y los muestra en formato de tabla.

    """

    datos = [None] * len(participantes)

    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = (p["j1"] + p["j2"] + p["j3"]) / 3
        promedio = int(promedio * 100) / 100

        fila = [None] * 5
        fila[0] = p["nombre"]
        fila[1] = p["j1"]
        fila[2] = p["j2"]
        fila[3] = p["j3"]
        fila[4] = promedio

        datos[i] = fila
        i = i + 1


    n = len(datos)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if datos[j][0] > datos[j + 1][0]:  
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux
            j = j + 1
        i = i + 1


    print("\n--- PARTICIPANTES ORDENADOS ALFABÉTICAMENTE ---")
    print("Nombre       | J1     | J2     | J3     | Promedio")
    print("---------------------------------------------------")

    k = 0
    while k < len(datos):
        fila = datos[k]

        nombre = fila[0]
        j1 = fila[1]
        j2 = fila[2]
        j3 = fila[3]
        promedio = fila[4]

        espacios = 13 - len(nombre)
        nombre_con_espacios = nombre + " " * espacios

        print(
            nombre_con_espacios + "|  " +
            str(j1) + "    |  " +
            str(j2) + "    |  " +
            str(j3) + "    |  " +
            str(promedio)
        )
        k = k + 1
