from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Return import *
from .Break import *

class Case(Instruccion) :

    def __init__(self, expresion, instrucciones, linea, columna) :
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :

        if not self.expresion is None:
            self.expresion.analizar(ts,mensajes)

        bandera = False
        for instruccion in self.instrucciones:
            if not bandera:
                instruccion.analizar(ts,mensajes)

                if isinstance(instruccion,Return) or isinstance(instruccion,Break):
                    bandera = True
            else:
                self.instrucciones.remove(instruccion)

    def get3D(self,ts) :
        c3d = ''

        for instruccion in self.instrucciones:
            c3d += str(instruccion.get3D(ts))

        return c3d

    def getAST(self) :
        ast = "\""+str(self)+"\" [label=\"ins_case\"] ;\n"
            
        if not self.expresion is None:
            ast+= "   \""+str(self)+"et"+"\" [label=\"case\"] ;\n"
            ast+= "   \""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"
            ast += self.expresion.getAST()
            ast+= "   \""+str(self)+"\" -> \""+str(self.expresion)+"\"\n"
        else:
            ast+= "   \""+str(self)+"et"+"\" [label=\"default\"] ;\n"
            ast+= "   \""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"

        ast += "\""+str(self.instrucciones)+"\" [label=\"instrucciones\"] ;\n"
        ast += "\""+str(self)+"\" -> \""+str(self.instrucciones)+"\"\n"

        for instruccion in self.instrucciones:
            ast += "\""+str(instruccion)+"\" [label=\"instruccion\"] ;\n"
            ast += "\""+str(self.instrucciones)+"\" -> \""+str(instruccion)+"\"\n"   

        return ast