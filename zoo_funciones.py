# funciones
import os


def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_cabecera():
    borrar_pantalla()
    cabecera = """
    ***********************************
    *                                 *
    *     Bienvenido al Zoo IS101     *
    *                                 *
    ***********************************
    """
    print(cabecera)

def verificar_edad(edad):
    """
    devolveremos una tupla, primera parte de la tupla será bool edad_Valida y
    edad_int será un int edad (positivo o negativo) y None para un ValuError
    """

    edadVerificada = (False, None)
    
    if edad == "":
        edadVerificada = (None, None)  # Indica que no se ha introducido ninguna edad y devuelve None para salirse
    else:
        try:
            edad_int = int(edad)
            if edad_int < 0:
                edadVerificada = (False, edad_int)  # Edad negativa
            else:
                edadVerificada = (True, edad_int)  # Edad válida
        except ValueError:
            edadVerificada = (False, None)  # Error por valor no numérico
    
    return edadVerificada




def resumen_parcial(tipos_entrada):
    entradas = [] 
        
    for tipo, valores in tipos_entrada.items():
        if valores['CONTADOR'] > 0:
            entrada = f"{valores['CONTADOR']} de {tipo}"
            entradas.append(entrada)
    
    if len(entradas) == 0:
        resumen = "Ninguna entrada seleccionada"
    else:
        resumen = ", ".join(entradas)
    
    return f"\nLlevas: {resumen}"

def imprimir_ticket(tipos_entrada):
    total = 0
    print_cabecera()
    print("\tTICKET ZOO IS101\n")
    for tipo, valores in tipos_entrada.items():
            if valores['CONTADOR'] > 0:
                subtotal = valores['CONTADOR'] * valores['PRECIO']
                print(f"\t{valores['CONTADOR']} de {tipo:<8}: {subtotal:7.2f} Euros") 
                total += subtotal 
    if total > 0:
        print("\t____________________________")
        print(f"\tTotal: {total:15.2f} Euros.\n")
    else:
        print("\tNo hay entradas seleccionadas.\n")