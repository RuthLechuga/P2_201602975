from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class For(Instruccion) :

    def __init__(self, declaracion, condicion, incremento, instrucciones, linea, columna) :
        self.declaracion = declaracion
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        if (not isinstance(self.declaracion,str)) and (not self.declaracion is None):
            self.declaracion.analizar(ts,mensajes)

        if not self.condicion is None:
            self.condicion.analizar(ts,mensajes)

        if not self.incremento is None:
            self.incremento.analizar(ts,mensajes)
        
        for instruccion in self.instrucciones:
            instruccion.analizar(ts,mensajes)

    def get3D(self,ts) :
        c3d = ''
        label_for = ts.getLabel()
        label_salida = ts.getLabel()

        c3d = '#inicializacion for:\n'
        c3d += self.declaracion.get3D(ts)

        c3d += label_for +':  #for \n'

        c3d += self.condicion.get3D(ts)
        et_expresion = ts.getTemporalActual()
        et_not_expresion = ts.getTemporal()
        c3d += et_not_expresion + ' = !'+et_expresion+';\n'

        c3d += 'if ('+et_not_expresion+') goto '+label_salida+';\n'

        for instruccion in self.instrucciones:
            c3d += instruccion.get3D(ts)

        c3d += '#incremento del for:\n'
        c3d += self.incremento.get3D(ts)
        c3d += 'goto '+label_for+';\n\n'

        c3d += label_salida +':   #salida for \n'

        return c3d

    def getAST(self) :
        pass