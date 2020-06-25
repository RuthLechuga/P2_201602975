from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Continue(Instruccion) :

    def __init__(self) :
        pass

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        label_inicio = ts.et_inicio.pop()
        c3d = 'goto '+label_inicio+';  #continue\n'
        ts.et_inicio.append(label_inicio)
        return c3d

    def getAST(self) :
        ast =   """ \""""+str(self)+"""\" [label=\"ins_continue\"] ;\n
                \""""+str(self)+"""b\" [label=\"continue\"] ;\n
                \""""+str(self)+"""\" -> \""""+str(self)+"""b\"\n""";
        return ast;
