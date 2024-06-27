# Importar funciones del archivo zoo_funciones
from zoo_funciones import *

# Diccionario de tipos de entrada
tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

# Función
def procesar_edad_valida(edad_Valida, edad_int, tipos_entrada):
    """
    edad_Valida (bool or None): Indica si la edad introducida es válida (True), inválida (False) o se ha finalizado el programa (None).
    edad_int (int or None): Edad convertida a entero si es válida, a entero negativo si es negativa, o None si no se introdujo ninguna edad.
    tipos_entrada (diccionario): Diccionario que contiene los tipos de entrada al zoo con sus respectivos límites de edad, precios y contadores.
    """
    if edad_Valida:
        for tipo, valor in tipos_entrada.items():
            if edad_int < valor["EDAD"]:
                valor["CONTADOR"] += 1
                break
    print_cabecera()
    print(resumen_parcial(tipos_entrada))
    
    if not edad_Valida and edad_int != None:
        print("\nError: No puede ser edad negativa.")
    elif not edad_Valida:
        print("\nError: Edad introducida no válida.")


# Cabecera del programa
print_cabecera()

# Inicio del bucle para pedir edades
while True:
    edad = input("\nEdad (pulsa enter para finalizar): ")
    edad_Valida, edad_int = verificar_edad(edad)
    if edad_Valida is None:
        break
    else:
        procesar_edad_valida(edad_Valida, edad_int, tipos_entrada)

# Mostrar la información final por pantalla
borrar_pantalla()
imprimir_ticket(tipos_entrada)
