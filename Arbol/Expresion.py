from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class TIPO_OPERACION(Enum) :
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    RESIDUO = 5,
    AND = 6
    OR = 7
    BBAND = 8
    BBOR = 9
    BBXOR = 10
    BBIZQ = 11
    BBDER = 12
    IGUAL_QUE = 13
    DISTINTO_QUE = 14
    MENOR_QUE = 15
    MAYOR_QUE = 16
    MENOR_IGUAL_QUE = 17
    MAYOR_IGUAL_QUE = 18
    NOT = 19
    BBNOT = 20
    PRE_INC = 21
    PRE_DEC = 22
    POST_INC = 23
    POST_DEC = 24
    ACCESO_ARREGLO = 25
    ACCESOS = 26
    ENTERO = 27
    DECIMAL = 28
    CADENA = 29
    CARACTER = 30
    IDENTIFICADOR = 31
    LLAMADA = 32
    TERNARIO = 33
    

class Expresion(Instruccion) :

    def __init__(self, izquierdo, derecha, tipo, linea, columna) :
        self.izquierdo = izquierdo
        self.derecha = derecha
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        if self.tipo == TIPO_OPERACION.ENTERO:
            return TIPO_DATO.ENTERO
        
        if self.tipo == TIPO_OPERACION.DECIMAL:
            return TIPO_DATO.DECIMAL
        
        if self.tipo == TIPO_OPERACION.CARACTER:
            return TIPO_DATO.CARACTER
        
        if self.tipo == TIPO_OPERACION.IDENTIFICADOR:
            temp = ts.getSimbolo(self.izquierdo)

            if temp is None:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador: '+ self.izquierdo+ ' no existe en el contexto actual.',self.linea,self.columna))
                return None
            
            return temp.tipo
        
        tipo_izq = None if self.izquierdo is None else self.izquierdo.analizar(ts,mensajes)
        tipo_der = None if self.derecha is None else self.derecha.analizar(ts,mensajes)


    def get3D(self,ts) :
        c3d = ""
        if self.tipo == TIPO_OPERACION.ENTERO or self.tipo == TIPO_OPERACION.DECIMAL:
            temporal = ts.getTemporal()
            c3d = temporal + ' = ' + str(self.izquierdo) + ';\n'
        
        elif self.tipo == TIPO_OPERACION.CARACTER:
            temporal = ts.getTemporal()
            c3d = temporal + ' = \'' + str(self.izquierdo) + '\';\n'
        
        elif self.tipo == TIPO_OPERACION.IDENTIFICADOR:
            var = ts.getSimbolo(self.izquierdo)
            temporal = ts.getTemporal()
            c3d = temporal + ' = ' + var.temporal + ';\n'

        return c3d

    def getAST(self) :
        pass