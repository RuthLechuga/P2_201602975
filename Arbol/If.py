from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class If(Instruccion) :

    def __init__(self, lista_if) :
        self.lista_if = lista_if

    def analizar(self,ts,mensajes) :
        for eif in self.lista_if:
            eif.analizar(ts,mensajes)        

    def get3D(self,ts) :
        c3d = ''
        et_salida = ts.getLabel() 

        for eif in self.lista_if:
            c3d += eif.get3D(ts)
            c3d += 'goto '+et_salida+';\n'

            if not eif.condicion is None:
                c3d += ts.getLabelActual() + ': \n'
        
        c3d += et_salida+':\n'

        return c3d

    def getAST(self) :
        ast = "   \""+str(self)+"\" [label=\"ins_ifs\"] ;\n";

        for elseif in self.lista_if:
            ast += "\""+str(self)+"\" -> \""+str(elseif)+"\"\n";
            ast += elseif.getAST();

        return ast