from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Struct(Instruccion) :

    def __init__(self,identificador,atributos,linea,columna) :
        self.identificador = identificador
        self.atributos = atributos
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        c3d = ''
        return c3d

    def getAST(self) :
        return ''
