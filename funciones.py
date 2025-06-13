# Parcial de Programación - Funciones para gestionar participantes

from inputs import pedir_nombre, pedir_puntaje


# Funcion auxiliar para calcular el promedio de un participante
def calcular_promedio(p):
    """
    Calcula y devuelve el promedio de un participante redondeado a 2 decimales.
    """
    suma = participante[1] + participante[2] + participante[3]
    promedio = suma / 3
    int(promedio * 100) / 100
    return promedio


from inputs import pedir_nombre

def cargar_participantes(cantidad):
    """
    Carga cantidad de participantes y los devuelve en una lista.
    Cada participante es una lista: [nombre, None, None, None]
    """
    participantes = [None] * cantidad
    i = 0
    while i < cantidad:
        nombre = pedir_nombre()
        participantes[i] = [nombre, None, None, None]
        i += 1
    return participantes



def cargar_puntuaciones(participantes):
    """
    Carga las puntuaciones de los tres jurados para cada participante.
    Usa la función pedir_puntaje() para validar los valores.
    """
    i = 0
    while i < len(participantes):
        nombre = participantes[i][0]
        print(f"\nIngresá los puntajes para {nombre}:")
        participantes[i][1] = pedir_puntaje("Jurado 1")
        participantes[i][2] = pedir_puntaje("Jurado 2")
        participantes[i][3] = pedir_puntaje("Jurado 3")
        i += 1
    print("Puntuaciones cargadas correctamente.")
    return True


def mostrar_puntajes(participantes):
    """
    Muestra el nombre y puntajes de cada jurado y el promedio del participante.
    Devuelve True si muestra correctamente.
    """
    print("\n--- PUNTAJES Y PROMEDIOS ---")
    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = calcular_promedio(p)
        print(f"\nParticipante: {p[0]}")
        print(f"  Jurado 1: {p[1]}")
        print(f"  Jurado 2: {p[2]}")
        print(f"  Jurado 3: {p[3]}")
        print(f"  Promedio: {promedio:.2f}")
        i += 1
    return True


def mostrar_promedios_menores_a_4(participantes):
    """
    Muestra participantes con promedio menor a 4. Devuelve la cantidad encontrada.
    """
    encontrados = 0
    print("\n--- Participantes con promedio menor a 4 ---")
    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = calcular_promedio(p)
        if promedio < 4:
            print(f"{p[0]} - Promedio: {promedio:.2f}")
            encontrados += 1
        i += 1

    if encontrados == 0:
        print("No hay participantes con promedio menor a 4.")
    return encontrados


def mostrar_promedios_menores_a_8(participantes):
    """
    Muestra participantes con promedio menor a 8. Devuelve la cantidad encontrada.
    """
    encontrados = 0
    print("\n--- Participantes con promedio menor a 8 ---")
    i = 0
    while i < len(participantes):
        p = participantes[i]
        promedio = calcular_promedio(p)
        if promedio < 8:
            print(f"{p[0]} - Promedio: {promedio:.2f}")
            encontrados += 1
        i += 1

    if encontrados == 0:
        print("No hay participantes con promedio menor a 8.")
    return encontrados

def promedio_por_jurado(participantes):
    """
    Calcula y muestra el promedio general de cada jurado.
    """
    
    total_j1 = 0
    total_j2 = 0
    total_j3 = 0
    cantidad = len(participantes)

    i = 0
    while i < cantidad:
        total_j1 += participantes[i][1]
        total_j2 += participantes[i][2]
        total_j3 += participantes[i][3]
        i += 1

    prom1 = int((total_j1 / cantidad) * 100) / 100
    prom2 = int((total_j2 / cantidad) * 100) / 100
    prom3 = int((total_j3 / cantidad) * 100) / 100

    print("\n--- Promedio de cada jurado ---")
    print(f"Jurado 1: {prom1}")
    print(f"Jurado 2: {prom2}")
    print(f"Jurado 3: {prom3}")

    return [prom1, prom2, prom3]

def jurado_mas_estricto(participantes):
    """
    Muestra todos los jurados que tengan el promedio más bajo.
    Usa la función promedio_por_jurado para obtener los promedios.
    """
    promedios = promedio_por_jurado(participantes)
    minimo = promedios[0]
    if promedios[1] < minimo:
        minimo = promedios[1]
    if promedios[2] < minimo:
        minimo = promedios[2]

    print("\n--- Jurado/s más estricto/s ---")
    if promedios[0] == minimo:
        print("Jurado 1 con promedio de", promedios[0])
    if promedios[1] == minimo:
        print("Jurado 2 con promedio de", promedios[1])
    if promedios[2] == minimo:
        print("Jurado 3 con promedio de", promedios[2])

    return True

def jurado_mas_generoso(participantes):
    """
    Muestra el o los jurados con el promedio más alto.
    Devuelve la cantidad de jurados que coinciden como más generosos.
    """

    promedios = promedio_por_jurado(participantes)  

    maximo = promedios[0]
    i = 1
    while i < 3:
        if promedios[i] > maximo:
            maximo = promedios[i]
        i += 1

    jurados = [0, 0, 0]  
    cantidad = 0

    i = 0
    while i < 3:
        if promedios[i] == maximo:
            jurados[cantidad] = i + 1  
            cantidad += 1
        i += 1

    print("\n--- Jurado/s más generoso/s ---")
    i = 0
    while i < cantidad:
        print(f"Jurado {jurados[i]} con promedio de {maximo}")
        i += 1

    return cantidad

def mostrar_puntajes_iguales(participantes):
    """
    Muestra los participantes que recibieron las mismas 3 puntuaciones.
    Devuelve la cantidad encontrada.
    """
    encontrados = 0

    print("\n--- Participantes con los 3 puntajes iguales ---")

    i = 0
    while i < len(participantes):
        j1 = participantes[i][1]
        j2 = participantes[i][2]
        j3 = participantes[i][3]

        if j1 == j2 and j2 == j3:
            print(f"{participantes[i][0]} - Puntaje: {j1}")
            encontrados += 1
        i += 1

    if encontrados == 0:
        print("No hay participantes con puntajes iguales entre los tres jurados.")

    return encontrados

def buscar_participante_por_nombre(participantes):
    """
    Permite buscar un participante por nombre e imprime sus datos si existe.
    Devuelve True si lo encuentra, False si no.
    """

    nombre_buscado = input("Ingresá el nombre que querés buscar: ")
    encontrado = False
    i = 0

    while i < len(participantes):
        nombre_actual = participantes[i][0]

        
        iguales = True
        if len(nombre_buscado) != len(nombre_actual):
            iguales = False
        else:
            j = 0
            while j < len(nombre_buscado):
                letra1 = nombre_buscado[j]
                letra2 = nombre_actual[j]

                if "A" <= letra1 <= "Z":
                    letra1 = chr(ord(letra1) + 32)  # convertir a minúscula
                if "A" <= letra2 <= "Z":
                    letra2 = chr(ord(letra2) + 32)

                if letra1 != letra2:
                    iguales = False
                j += 1

        if iguales:
            promedio = calcular_promedio(participantes[i])
            print("\n--- Participante encontrado ---")
            print(f"Nombre: {participantes[i][0]}")
            print(f"Jurado 1: {participantes[i][1]}")
            print(f"Jurado 2: {participantes[i][2]}")
            print(f"Jurado 3: {participantes[i][3]}")
            print(f"Promedio: {promedio:.2f}")
            encontrado = True
        i += 1

    if not encontrado:
        print("No se encontró un participante con ese nombre.")

    return encontrado





def mostrar_top3(participantes):
    """
    Muestra los 3 participantes con mayor promedio.
    Usa burbuja para ordenar de mayor a menor.
    Devuelve True si muestra correctamente.
    """

    
    ordenados = [None] * len(participantes)

    i = 0
    while i < len(participantes):
        fila = [None] * 5
        j = 0
        while j < 4:
            fila[j] = participantes[i][j]
            j += 1
        fila[4] = calcular_promedio(participantes[i])
        ordenados[i] = fila
        i += 1

    
    n = len(ordenados)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if ordenados[j][4] < ordenados[j+1][4]:
                aux = ordenados[j]
                ordenados[j] = ordenados[j+1]
                ordenados[j+1] = aux
            j += 1
        i += 1

    
    print("\n--- TOP 3 Participantes con mayor promedio ---")
    i = 0
    while i < 3 and i < len(ordenados):
        print(f"{ordenados[i][0]} - Promedio: {ordenados[i][4]:.2f}")
        i += 1

    return True






def mostrar_ordenados_alfabeticamente(participantes):
    """
    Muestra los participantes ordenados por nombre de A a Z.
    Devuelve True si funciona correctamente.
    """

    
    ordenados = [None] * len(participantes)

    i = 0
    while i < len(participantes):
        fila = [None] * 5
        j = 0
        while j < 4:
            fila[j] = participantes[i][j]
            j += 1
        fila[4] = calcular_promedio(participantes[i])
        ordenados[i] = fila
        i += 1

    
    n = len(ordenados)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if ordenados[j][0] > ordenados[j+1][0]:
                aux = ordenados[j]
                ordenados[j] = ordenados[j+1]
                ordenados[j+1] = aux
            j += 1
        i += 1

    print("\n--- Participantes ordenados alfabéticamente ---")
    i = 0
    while i < len(ordenados):
        print(f"{ordenados[i][0]} - Notas: {ordenados[i][1]}, {ordenados[i][2]}, {ordenados[i][3]} - Promedio: {ordenados[i][4]:.2f}")
        i += 1

    return True


def mostrar_ganador(participantes):
    """
    Muestra al participante ganador (mayor promedio).
    Si hay más de uno con el mismo promedio, muestra un mensaje de empate.
    Devuelve la lista de ganadores (1 o más).
    """
    i = 0
    mejor_promedio = calcular_promedio(participantes[0])

    
    while i < len(participantes):
        promedio = calcular_promedio(participantes[i])
        if promedio > mejor_promedio:
            mejor_promedio = promedio
        i += 1

    
    ganadores = [None] * len(participantes)
    cantidad = 0
    i = 0
    while i < len(participantes):
        if calcular_promedio(participantes[i]) == mejor_promedio:
            ganadores[cantidad] = participantes[i]
            cantidad += 1
        i += 1

    print("\n--- GANADOR DE LA COMPETENCIA ---")
    if cantidad == 1:
        print(f"El ganador es {ganadores[0][0]} con un promedio de {mejor_promedio:.2f}")
    else:
        print(f"Hay {cantidad} participantes empatados con promedio {mejor_promedio:.2f}.")
        print("Se requiere realizar un desempate entre:")
        j = 0
        while j < cantidad:
            print(f"- {ganadores[j][0]}")
            j += 1

    
    ganadores_definitivos = [None] * cantidad
    j = 0
    while j < cantidad:
        ganadores_definitivos[j] = ganadores[j]
        j += 1

    return ganadores_definitivos

import random

def resolver_empate(ganadores):
    """
    Recibe una lista de participantes empatados y elige uno aleatoriamente.
    Devuelve el nombre del ganador seleccionado.
    """
    if len(ganadores) <= 1:
        print("No hay empate para resolver.")
        return None

    
    indice = random.randint(0, len(ganadores) - 1)
    ganador = ganadores[indice][0]

    print("\n--- DESEMPATE ---")
    print(f"El ganador por desempate es: {ganador}")

    return ganador