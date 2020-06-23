from .Instruccion import Instruccion
from .Mensaje import *

class TIPO_FUNCION(Enum) :
    ENTERO = 1
    DECIMAL = 2
    CARACTER = 4
    VOID = 4

class Funcion(Instruccion) :

    def __init__(self,tipo,identificador,parametros,instrucciones,linea,columna) :
        self.tipo = tipo
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        pass
    
    def get3D(self,ts):
        pass

    def getAST(self):
        pass