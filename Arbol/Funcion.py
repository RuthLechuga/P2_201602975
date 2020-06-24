from .Instruccion import Instruccion
from .Mensaje import *

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

    def analizar(self,ts,mensajes) :
        ambito_actual = ts.ambito
        
        #valida que la función no exista en el contexto actual
        if not ts.addFuncion(self):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La función: '+ self.identificador+ ' ya existe.',self.linea,self.columna))
            return
        
        #se agregan los parametros a la tabla de simbolos
        ts.ambito = self.identificador

        if not self.parametros is None:
            print(">>validar funciones con parametros :D")
        
        #se analizan las instrucciones de la funcion
        if not self.instrucciones is None:
            for instruccion in self.instrucciones:
                instruccion.analizar(ts,mensajes)
        
        ts.ambito = ambito_actual
    
    def get3D(self,ts):
        c3d = self.identificador + ':\n'

        ambito_actual = ts.ambito
        ts.ambito = self.identificador

        if not self.parametros is None:
            print(">>validar funciones con parametros :D")
        
        if not self.instrucciones is None:
            for instruccion in self.instrucciones:
                c3d += instruccion.get3D(ts)

        ts.ambito = ambito_actual
        return c3d

    def getAST(self):
        pass