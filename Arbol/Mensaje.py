from enum import Enum

class TIPO_MENSAJE(Enum) :
    LEXICO = 1,
    SINTACTICO = 2,
    SEMANTICO = 3,
    LOG = 4

class Mensaje() :
    def __init__(self, tipo_mensaje, mensaje, linea, columna):
        self.tipo_mensaje = tipo_mensaje
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna