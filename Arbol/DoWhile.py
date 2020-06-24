from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class DoWhile(Instruccion) :

    def __init__(self, expresion, instrucciones, linea, columna) :
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        
        if not self.expresion.analizar(ts,mensajes) == TIPO_DATO.ENTERO :
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La condición para el While es incorrecta.',self.linea,self.columna))
            
        for instruccion in self.instrucciones:
            instruccion.analizar(ts,mensajes)

    def get3D(self,ts) :
        c3d = ''
        label_do_while = ts.getLabel()
        label_salida = ts.getLabel()

        c3d = label_do_while +':  #do-while \n'

        for instruccion in self.instrucciones:
            c3d += instruccion.get3D(ts)

        c3d += self.expresion.get3D(ts)
        et_expresion = ts.getTemporalActual()
        c3d += 'if ('+et_expresion+') goto '+label_do_while+';\n'

        c3d += label_salida +':   #salida do-while \n'

        return c3d

    def getAST(self) :
        pass