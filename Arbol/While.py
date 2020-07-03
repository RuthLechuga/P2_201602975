from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Return import *
from .Break import *
from .Continue import *

class While(Instruccion) :

    def __init__(self, expresion, instrucciones, linea, columna) :
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        
        if not self.expresion.analizar(ts,mensajes) == TIPO_DATO.ENTERO :
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La condición para el While es incorrecta.',self.linea,self.columna))
        
        bandera = False
        for instruccion in self.instrucciones:
            if not bandera:
                instruccion.analizar(ts,mensajes)

                if isinstance(instruccion,Return) or isinstance(instruccion,Break) or isinstance(instruccion,Continue):
                    bandera = True
            else:
                self.instrucciones.remove(instruccion)

    def get3D(self,ts) :
        c3d = ''
        label_while = ts.getLabel()
        label_salida = ts.getLabel()
        
        ts.et_salida.append(label_salida)
        ts.et_inicio.append(label_while)

        c3d = label_while +':  #while \n'

        c3d += self.expresion.get3D(ts)
        et_expresion = ts.getTemporalActual()
        et_not_expresion = ts.getTemporal()
        c3d += et_not_expresion + ' = !'+et_expresion+';\n'

        c3d += 'if ('+et_not_expresion+') goto '+label_salida+';\n'

        for instruccion in self.instrucciones:
            c3d += instruccion.get3D(ts)

        c3d += 'goto '+label_while+';\n\n'

        c3d += label_salida +':   #salida while \n'

        ts.et_salida.pop()
        ts.et_inicio.pop()
        return c3d

    def getAST(self) :
        ast = "   \""+str(self)+"\" [label=\"ins_while\"] ;\n" + \
              "   \""+str(self)+"et"+"\" [label=\"while\"] ;\n" + \
              "   \""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"
        
        ast += self.expresion.getAST();
        ast += "\""+str(self)+"\" -> \""+str(self.expresion)+"\"\n";

        ast += "\""+str(self.instrucciones)+"\" [label=\"instrucciones\"] ;\n";
        ast += "\""+str(self)+"\" -> \""+str(self.instrucciones)+"\"\n";

        for instruccion in self.instrucciones:
            ast += "\""+str(instruccion)+"\" [label=\"instruccion\"] ;\n";
            ast += "\""+str(self.instrucciones)+"\" -> \""+str(instruccion)+"\"\n";
            ast += instruccion.getAST()

        return ast