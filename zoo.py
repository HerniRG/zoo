"""
Enunciado 

Un zoo fija el precio de la entrada según la edad del visitante, así:

    los niños de 2 años o menos no pagan
    los niños de 3 a 12 pagan 14$
    A partir de los 13 años se considera entrada de adulto por un valor de 23$
    Los jubilados, 65 o más años pagan 18$

Debes hacer un programa que pida las edades del grupo que va a visitar el zoo y devolver el precio del grupo y el detalle por edades.

El programa devolverá el cálculo y el detalle cuando no se introduzcan más edades, es decir, se introduzca ''.

Debes asegurarte de que la edad sea un número entro y positivo.
"""

"""
Documentación justificación texto Python https://docs.python.org/es/3/tutorial/inputoutput.html
Comando borrado pantalla (buscado en google): os.system('cls' if os.name == 'nt' else 'clear')
"""

import os

# iniciar edad
edad = 0

# diccionario entradas zoo
tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

# funciones
def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def resumen_parcial(tipos_entrada):
    entradas = [] 

    for tipo, valores in tipos_entrada.items():
        if valores['CONTADOR'] > 0:
            entrada = f"{valores['CONTADOR']} de {tipo}"
            entradas.append(entrada)
    
    resumen = ", ".join(entradas)
    
    return f"Llevas: {resumen}\n"

def imprimir_ticket():
    total = 0
    print("TICKET ZOO IS101\n")
    for tipo, valores in tipos_entrada.items():
            if valores['CONTADOR'] > 0:
                subtotal = valores['CONTADOR'] * valores['PRECIO']
                print(f"{valores['CONTADOR']} de {tipo:<8}: {subtotal:7.2f} Euros") 
                total += subtotal 
    if total > 0:
        print("_"*28)
        print(f"Total: {total:15.2f} Euros")
    else:
        print("No hay entradas seleccionadas.")
         


# cabecera programa
borrar_pantalla()
print("Bievenido al Zoo IS101\n")

# inicio bucle, peticion edades y suma contadores
while True:
    edad = input("Edad: ")
    borrar_pantalla()
    if edad == "":
        break
    else:
        try:
            edad = int(edad)
            if edad < 0:
                    raise ValueError("No puede ser edad negativa.")
            for tipo, valor in tipos_entrada.items():
                if edad < valor["EDAD"]:
                    valor["CONTADOR"] += 1
                    break            

            print(resumen_parcial(tipos_entrada))
            
        except:
            print("Error: Edad introducida no válida.\n")

# muestra de información por pantalla
borrar_pantalla()
imprimir_ticket()