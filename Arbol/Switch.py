from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Expresion import *

class Switch(Instruccion) :

    def __init__(self,expresion,cases,linea,columna) :
        self.expresion = expresion
        self.cases = cases
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        self.expresion.analizar(ts,mensajes)

        for case in self.cases:
            case.analizar(ts,mensajes)

    def get3D(self,ts) :
        c3d = ''
        et_salida = ts.getLabel() 
        ts.et_salida.append(et_salida)

        et_cases = []

        for case in self.cases:
            label = ts.getLabel()
            et_cases.append(label)

            if not case.expresion is None:
                temp_cond = Expresion(self.expresion,case.expresion,TIPO_OPERACION.IGUAL_QUE,self.linea,self.columna,'==')
                c3d += temp_cond.get3D(ts)
                temporal = ts.getTemporalActual()
                c3d += 'if('+temporal+') goto '+label+';\n'
            else:
                c3d += 'goto '+label+';\n'
        
        for pos in range(0,len(self.cases)):
            c3d += et_cases[pos] + ': \n'
            c3d += self.cases[pos].get3D(ts)

                    
        c3d += et_salida+':\n'

        ts.et_salida.pop()
        return c3d

    def getAST(self) :
        pass