from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Break(Instruccion) :

    def __init__(self) :
        pass

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        label_salida = ts.et_salida.pop()
        c3d = 'goto '+label_salida+';  #break\n'
        ts.et_salida.append(label_salida)
        return c3d

    def getAST(self) :
        ast =   """ \""""+str(self)+"""\" [label=\"ins_break\"] ;\n
                \""""+str(self)+"""b\" [label=\"break\"] ;\n
                \""""+str(self)+"""\" -> \""""+str(self)+"""b\"\n"""
        return ast
