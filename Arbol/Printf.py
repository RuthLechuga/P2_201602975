from .Instruccion import Instruccion
from .Mensaje import *

class Printf(Instruccion) :

    def __init__(self, cadena, parametros, linea, columna) :
        self.cadena = cadena
        self.parametros = parametros
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        pass

    def getAST(self) :
        pass