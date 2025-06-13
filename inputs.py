def pedir_nombre():
    """
    Solicita al usuario un nombre válido (mínimo 3 caracteres, solo letras y espacios).
    Devuelve el nombre si es válido.
    """
    while True:
        nombre = input("Ingresá el nombre del participante: ")
        if len(nombre) >= 3:
            valido = True
            i = 0
            while i < len(nombre):
                letra = nombre[i]
                if not ("A" <= letra <= "Z" or "a" <= letra <= "z" or letra == " " or 
                        
                        letra == "Ñ" or letra == "ñ" or
                        letra == "á" or letra == "é" or letra == "í" or letra == "ó" or letra == "ú" or
                        letra == "Á" or letra == "É" or letra == "Í" or letra == "Ó" or letra == "Ú"):
                    valido = False
                i = i + 1
            if valido:
                return nombre
        print("Nombre inválido. Debe tener al menos 3 letras y solo letras o espacios.")
    

def pedir_puntaje(jurado):
    """
    Pide un puntaje para un jurado.
    Valida que sea un número entero entre 1 y 10.
    Devuelve el puntaje como entero.
    """
    while True:
        entrada = input("Ingresá el puntaje para " + jurado + ": ")

        es_numero = True
        i = 0

        if len(entrada) == 0:
            es_numero = False

        while i < len(entrada):
            if not ("0" <= entrada[i] <= "9"):
                es_numero = False
            i += 1

        if es_numero:
            puntaje = int(entrada)
            if 1 <= puntaje <= 10:
                return puntaje
            else:
                print("El puntaje debe estar entre 1 y 10.")
        else:
            print("Entrada inválida. Ingresá un número del 1 al 10.")