from enum import Enum

class TIPO_DATO(Enum) :
    ENTERO = 1
    DECIMAL = 2
    CARACTER = 3
    ARREGLO = 4
    STRUCT = 5

class Simbolo() :
    def __init__(self, identificador, tipo, dimension, linea, columna, ambito, temporal="") :
        self.identificador = identificador
        self.tipo = tipo
        self.dimension = dimension
        self.linea = linea
        self.columna = columna
        self.ambito = ambito
        self.temporal = temporal