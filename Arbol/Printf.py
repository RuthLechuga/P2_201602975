from .Instruccion import Instruccion
from .Mensaje import *

class Printf(Instruccion) :

    def __init__(self, cadena, parametros, linea, columna) :
        self.cadena = cadena
        self.parametros = parametros
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        if not self.parametros is None:
            for parametro in self.parametros:
                parametro.analizar(ts,mensajes)    

    def get3D(self,ts) :
        c3d = ''

        if self.parametros is None:
            c3d = 'print(\"'+self.cadena+'\");\n'
        else:
            temp_cad = ''
            total = len(self.cadena)
            pos = 0
            pos_param = 0

            while pos < total:
                if self.cadena[pos] != '%':
                    temp_cad+= self.cadena[pos]
                
                else:
                    c3d += 'print(\"'+temp_cad+'\");\n'
                    temp_cad = ''
                    pos +=1

                    if pos_param<len(self.parametros):
                        c3d += self.parametros[pos_param].get3D(ts)

                        if self.cadena[pos]!='c':
                            c3d += 'print('+ts.getTemporalActual()+');\n'
                        else:
                            c3d += ts.getTemporalActual() +'= (char)'+ts.getTemporalActual()+';\n';
                            c3d += 'print('+ts.getTemporalActual()+');\n'

                        pos_param +=1
                    else:
                        c3d += 'print(0);\n'
                pos+=1
            
            if len(temp_cad)>0:
                c3d += 'print(\"'+temp_cad+'\");\n'

        return c3d

    def getAST(self) :
        pass