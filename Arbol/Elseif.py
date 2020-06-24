from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Elseif(Instruccion) :

    def __init__(self, expresion, instrucciones, linea, columna) :
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        pass        

    def get3D(self,ts) :
        c3d = ''
        return c3d

    def getAST(self) :
        pass