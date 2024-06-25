"""
Ejercicio 3. Grupo en el zoo
Enunciado

Un zoo fija el precio de la entrada según la edad del visitante, así:

    los niños de 2 años o menos no pagan
    los niños de 3 a 12 pagan 14€
    A partir de 13 años se considera entrada de adulto por un valor de 23 €
    Los jubilados, 65 o más años pagan 18 €

Debes hacer un programa que pida las edades del grupo que va a visitar el zoo y devolver el precio del grupo y el detalle por edades.

El programa devolverá el cálculo y el detalle cuando no se introduzcan más edades, es decir se introduzca ''.

Debes asegurarte de que la edad sea un número entero y positivo.
"""

"""
preguntar edad -> edad
lista_edades = []

While edad != '':
    lista_edades.append(edad)

"""
lista = []
precios = []
contador_edades = [0, 0, 0, 0]
grupos_edad = ['BEBES', 'NIÑOS', 'ADULTOS', 'JUBILADOS']
edad = 0



while edad != '':
    edad = int(input("Edad: ")) # Explotara? pregunta Maria
    lista.append(edad)
    #procesar edad
    if edad < 3:
        precios.append(0)
        contador_edades[0] += 1
    elif edad < 13:
        precios.append(14)
        contador_edades[1] += 1
    elif edad < 65:
        precios.append(23)
        contador_edades[2] += 1
    else:
        precios.append(18)
        contador_edades[3] +=1


# Visualizar datos
precio_final = 0
for precio in precios:
    precio_final += precio

print(f"Precio total: {precio_final:.2f}")
indice = 0
while indice <= len(lista):
    print(f"{contador_edades[indice]} entradas de {grupos_edad[indice]}")
    indice += 1

for i in range(4):
    print(f"{contador_edades[indice]} entradas de {grupos_edad[indice]}")
