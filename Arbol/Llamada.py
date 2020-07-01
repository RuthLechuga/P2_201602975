from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Asignacion import *
from .Funcion import *

class Llamada(Instruccion) :

    def __init__(self, identificador, parametros, linea, columna) :
        self.identificador = identificador
        self.parametros = parametros
        self.linea = linea
        self.columna = columna
        self.asig_parametros = []

    def analizar(self,ts,mensajes) :
        funcion = ts.getFuncion(self.identificador)

        if funcion is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La función:'+self.identificador+' no ha sido declarada.',self.linea,self.columna))
            return
        
        if len(funcion.parametros) != len(self.parametros):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La cantidad de parametros de:'+self.identificador+' no coincide con la cantidad de parametros en la llamada.',self.linea,self.columna))
            return
        
        ambito_actual = ts.ambito
        ts.ambito = self.identificador
            
        for i in range(len(funcion.parametros)):
            temp_asig = Asignacion(funcion.parametros[i].identificador,None,'=',self.parametros[i],self.linea,self.columna)
            temp_asig.analizar(ts,mensajes)
            self.asig_parametros.append(temp_asig)
        
        ts.ambito = ambito_actual

        if funcion.tipo == TIPO_FUNCION.ENTERO:
            return TIPO_DATO.ENTERO
        if funcion.tipo == TIPO_FUNCION.DECIMAL:
            return TIPO_DATO.DECIMAL
        if funcion.tipo == TIPO_FUNCION.CARACTER:
            return TIPO_DATO.CARACTER
        return None

    def get3D(self,ts) :
        c3d =''

        funcion = ts.getFuncion(self.identificador)

        ambito_actual = ts.ambito
        ts.ambito = self.identificador

        for asignacion in self.asig_parametros:
            c3d += asignacion.get3D(ts)
            c3d += '$s2[$sp] ='+asignacion.temporal+';\n'
            c3d += '$sp=$sp+1;\n'
        
        pila = "$s1"
        cont = funcion.addCont()
        c3d += pila +'[$ra] ='+str(cont)+';\n'
        c3d += '$ra = $ra+1;\n'
        c3d += 'goto '+self.identificador+';\n'

        c3d += 'sig_'+self.identificador+'_'+str(cont)+':\n'
        
        if self.identificador == ambito_actual:
            i = len(self.asig_parametros)
            for asignacion in self.asig_parametros:
                temporal = ts.getTemporal()
                c3d += temporal+'=$sp-'+str(i)+';\n'
                c3d += asignacion.temporal+' =$s2['+temporal+'];\n'
                i-=1
        
        c3d += ts.getTemporal() + ' = '+funcion.var_retorno+';\n'
        
        ts.ambito = ambito_actual

        return c3d

    def getAST(self) :
        pass
