from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Return(Instruccion) :

    def __init__(self, expresion, linea, columna) :
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        if not self.expresion is None:
            return self.expresion.analizar(ts,mensajes)

    def get3D(self,ts) :
        funcion = ts.getFuncion(ts.ambito)
        c3d = ''

        if not self.expresion is None:
            c3d = self.expresion.get3D(ts)
            c3d += funcion.var_retorno + '=' + ts.getTemporalActual() + ';\n'
            c3d += '$sp = $sp - '+str(len(funcion.parametros))+';\n'
        
        c3d += 'goto end_'+ts.ambito+';\n'
            
        return c3d
            
    def getAST(self) :
        ast = "   \""+str(self)+"\" [label=\"ins_return\"] ;\n" + \
            "   \""+str(self)+"r\" [label=\"return\"] ;\n" + \
            "   \""+str(self)+"\" -> \""+str(self)+"r\"\n"
        
        if not self.expresion is None:
            ast += self.expresion.getAST()
            ast += "   \""+str(self)+"\" -> \""+str(self.expresion)+"\"\n";
 
        return ast