from .Instruccion import Instruccion
from .Mensaje import *
from .Return import *

class TIPO_FUNCION(Enum) :
    ENTERO = 1
    DECIMAL = 2
    CARACTER = 4
    VOID = 4

class Funcion(Instruccion) :

    def __init__(self,tipo,identificador,parametros,instrucciones,linea,columna) :
        self.tipo = tipo
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
        self.c3d_retorno = 'end_'+self.identificador+':\n$ra = $ra - 1;\n'
        self.cont_retornos = 0
        self.var_retorno = ''
    
    def addCont(self):
        self.cont_retornos += 1
        self.c3d_retorno += 'if($s1[$ra]=='+str(self.cont_retornos)+') goto sig_'+self.identificador+'_'+str(self.cont_retornos)+';\n'
        return self.cont_retornos

    def analizar(self,ts,mensajes) :
        ambito_actual = ts.ambito
        
        #valida que la función no exista en el contexto actual
        if not ts.addFuncion(self):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La función: '+ self.identificador+ ' ya existe.',self.linea,self.columna))
            return
        
        #se agregan los parametros a la tabla de simbolos
        ts.ambito = self.identificador

        if not self.parametros is None:
            for parametro in self.parametros:
                parametro.analizar(ts,mensajes)
        
        #se analizan las instrucciones de la funcion
        if not self.instrucciones is None:
            for instruccion in self.instrucciones:
                instruccion.analizar(ts,mensajes)
                
        self.var_retorno = ts.getRetorno()        
        ts.ambito = ambito_actual
    
    def get3D(self,ts):
        c3d=''
        if self.identificador.lower() != 'main':
            c3d = self.identificador + ':\n'

        ambito_actual = ts.ambito
        ts.ambito = self.identificador

        if not self.parametros is None:
            for parametro in self.parametros:
                parametro.get3D(ts)
        
        if self.identificador.lower() == 'main':
            c3d += '$s1 = array();\n'
            c3d += '$s2 = array();\n'
            c3d += '$ra = 0;\n'
            c3d += '$sp = 0;\n'
            for funcion in ts.funciones.values():
                c3d += funcion.var_retorno + '=0;\n'

        if not self.instrucciones is None:
            for instruccion in self.instrucciones:
                c3d += instruccion.get3D(ts)

        c3d += 'goto end_'+self.identificador+';\n'

        ts.ambito = ambito_actual
        return c3d

    def getAST(self):
        pass