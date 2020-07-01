from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Case(Instruccion) :

    def __init__(self, expresion, instrucciones, linea, columna) :
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :

        if not self.expresion is None:
            self.expresion.analizar(ts,mensajes)

        for instruccion in self.instrucciones:
            instruccion.analizar(ts,mensajes)

    def get3D(self,ts) :
        c3d = ''

        for instruccion in self.instrucciones:
            c3d += str(instruccion.get3D(ts))

        return c3d

    def getAST(self) :
        pass