# Importar funciones del archivo zoo_funciones
from zoo_funciones import *

# Diccionario de tipos de entrada
tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

# Cabecera del programa
print_cabecera()

# Inicio del bucle para pedir edades
while True:
    edad = input("\nEdad (pulsa enter para finalizar): ")
    edad_Valida, edad_int = verificar_edad(edad)
    if edad_Valida is None: # he puesto None si pulsamos "" (intro)
        break
    else:
        tipos_entrada = procesar_edad(edad_Valida, edad_int, tipos_entrada)

# Mostrar la información final por pantalla
borrar_pantalla()
imprimir_ticket(tipos_entrada)
