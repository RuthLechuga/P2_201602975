from .Instruccion import Instruccion

class Scanf(Instruccion) :

    def __init__(self, linea, columna) :
       self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        return ' read()'

    def getAST(self) :
        pass
