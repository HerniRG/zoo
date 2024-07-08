# Importar funciones del archivo zoo_funciones
from zoo_funciones import *
from simple_screen import Screen_manager, locate, pair
from simple_screen.entities import Color

with Screen_manager as sc:

    def main():
        pair(Color(255, 0, 0), Color(255, 255, 255) )
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
            edad = Input("\nEdad (pulsa enter para finalizar): ")
            edad_Valida, edad_int = verificar_edad(edad)
            if edad_Valida is None: # entra aqui porque verificar_edad marca None si usuario pulsa enter ""
                break
            else:
                tipos_entrada = procesar_edad(edad_Valida, edad_int, tipos_entrada)

        # Mostrar la información final por pantalla
        imprimir_ticket(tipos_entrada)
        Input("Pulsa cualquier tecla para finalizar el programa.")

    # Por si se importa para no ejecutarlo
    if __name__ == "__main__":
        main()
