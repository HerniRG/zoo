# funciones
import os
from simple_screen import Print, locate, Input, cls

"""
la justificación del texto para mostrarlo en pantalla lo miré en
Documentación Justificación Texto Python https://docs.python.org/es/3/tutorial/inputoutput.html
"""


def borrar_pantalla():
    cls()

def print_cabecera():
    borrar_pantalla()
    cabecera = """
    ***********************************
    *                                 *
    *     Bienvenido al Zoo IS101     *
    *                                 *
    ***********************************
    """
    Print(cabecera)

def verificar_edad(edad):
    """
    devolveremos una tupla, primera parte de la tupla (bool or None): Indica si la edad introducida es válida (True), inválida (False) o se ha finalizado el programa (None).
    y segunda parte (int or None): Edad convertida a entero si es válida, a entero negativo si es negativa, o None si no se introdujo ninguna edad válida.
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

def procesar_edad(edad_Valida, edad_int, tipos_entrada):
    """
    edad_Valida (bool or None): Indica si la edad introducida es válida (True), inválida (False) o se ha finalizado el programa (None).
    edad_int (int or None): Edad convertida a entero si es válida, a entero negativo si es negativa, o None si no se introdujo ninguna edad.
    tipos_entrada (diccionario): Diccionario que contiene los tipos de entrada al zoo con sus respectivos límites de edad, precios y contadores.
    devuelve tipos de entrada ya procesado
    """
    procesado_tipos_entrada = tipos_entrada
    if edad_Valida:
        for tipo, valor in procesado_tipos_entrada.items():
            if edad_int < valor["EDAD"]:
                valor["CONTADOR"] += 1
                break
    print_cabecera()
    Print(resumen_parcial(procesado_tipos_entrada))
    
    if not edad_Valida and edad_int != None:
        Print("\nError: No puede ser edad negativa.")
    elif not edad_Valida:
        Print("\nError: Edad introducida no válida.")
    
    return procesado_tipos_entrada


def resumen_parcial(tipos_entrada):
    """
    Recorre tipos_entrada y simplemente verifica si contador es mayor que 0 lo añade a lista 
    para despues mostrar información de como va la compra de entradas
    """

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
    """
    recorre tipos_entrada e imprime ticket, 
    tambien se tiene en cuenta si no se ha comprado ningún ticket
    """
    total_euros = 0
    total_tickets = 0 # He creado este porque se puede comprar X entradas a bebes y valer el total 0€. Para imprimir ticket en el caso de solo bebé
    
    borrar_pantalla()
    print_cabecera()
    Print("\tTICKET ZOO IS101\n")
    for tipo, valores in tipos_entrada.items():
            if valores['CONTADOR'] > 0:
                subtotal = valores['CONTADOR'] * valores['PRECIO']
                total_tickets += valores['CONTADOR']
                Print(f"\t{valores['CONTADOR']} de {tipo:<8}: {subtotal:7.2f} €") 
                total_euros += subtotal 
    if total_tickets > 0:
        Print("\t____________________________")
        Print(f"\tTotal: {total_euros:15.2f} €\n")
    else:
        Print("\tNo hay entradas seleccionadas.\n")