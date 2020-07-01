from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Acceso(Instruccion) :

    def __init__(self,identificador,accesos,linea,columna) :
        self.identificador = identificador
        self.accesos = accesos
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        simbolo = ts.getSimbolo(self.identificador)
        return simbolo.tipo

    def get3D(self,ts) :
        c3d = '' 
        return c3d

    def getAST(self) :
        return '';
