from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Llamada(Instruccion) :

    def __init__(self, identificador, parametros, linea, columna) :
        self.identificador = identificador
        self.parametros  parametros
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        c3d =''
        return c3d

    def getAST(self) :
        pass
