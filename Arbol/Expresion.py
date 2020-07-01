from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class TIPO_OPERACION(Enum) :
    SUMA = 1,                   #si
    RESTA = 2,                  #si
    MULTIPLICACION = 3,         #si
    DIVISION = 4,               #si
    RESIDUO = 5,                #si
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
    ENTERO = 27                 #si
    DECIMAL = 28                #si
    CADENA = 29         
    CARACTER = 30               #si
    IDENTIFICADOR = 31          #si
    LLAMADA = 32
    TERNARIO = 33
    MENOS_UNARIO = 34

class Expresion(Instruccion) :

    def __init__(self, izquierdo, derecha, tipo, linea, columna, signo='') :
        self.izquierdo = izquierdo
        self.derecha = derecha
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.signo = signo

    def analizar(self,ts,mensajes) :
        if self.tipo == TIPO_OPERACION.ENTERO:
            return TIPO_DATO.ENTERO
        
        if self.tipo == TIPO_OPERACION.DECIMAL:
            return TIPO_DATO.DECIMAL
        
        if self.tipo == TIPO_OPERACION.CARACTER:
            return TIPO_DATO.CARACTER
        
        if self.tipo == TIPO_OPERACION.CADENA:
            return TIPO_DATO.CADENA
        
        if self.tipo == TIPO_OPERACION.LLAMADA:
            return self.izquierdo.analizar(ts,mensajes)
        
        if self.tipo == TIPO_OPERACION.IDENTIFICADOR:
            temp = ts.getSimbolo(self.izquierdo)

            if temp is None:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador: '+ self.izquierdo+ ' no existe en el contexto actual.',self.linea,self.columna))
                return None
            
            return temp.tipo
        
        try:
            tipo_izq = None if self.izquierdo is None else self.izquierdo.analizar(ts,mensajes)
            tipo_der = None if self.derecha is None else self.derecha.analizar(ts,mensajes)
        except:
            return None

        if tipo_der is None:
            if (self.tipo == TIPO_OPERACION.NOT or self.tipo == TIPO_OPERACION.BBNOT) and tipo_izq == TIPO_DATO.ENTERO:
                return TIPO_DATO.ENTERO
            
            if (self.tipo == TIPO_OPERACION.MENOS_UNARIO):
                if (tipo_izq == TIPO_DATO.ENTERO or tipo_izq == TIPO_DATO.DECIMAL or tipo_izq == TIPO_DATO.CARACTER):
                    return tipo_izq
            
            if self.tipo == TIPO_OPERACION.LLAMADA:
                return tipo_izq

            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Incompatibilidad de tipo en la operación.',self.linea,self.columna))
            return None
        
        if self.tipo == TIPO_OPERACION.SUMA or self.tipo == TIPO_OPERACION.RESTA or self.tipo == TIPO_OPERACION.MULTIPLICACION or self.tipo == TIPO_OPERACION.DIVISION or self.tipo == TIPO_OPERACION.RESIDUO:
            
            if tipo_izq == TIPO_DATO.ENTERO and tipo_der == TIPO_DATO.ENTERO:
                return tipo_izq

            if tipo_izq == TIPO_DATO.ENTERO and tipo_der == TIPO_DATO.DECIMAL or tipo_izq == TIPO_DATO.DECIMAL and tipo_der == TIPO_DATO.ENTERO or tipo_izq == TIPO_DATO.DECIMAL and tipo_der == TIPO_DATO.DECIMAL:
                return TIPO_DATO.DECIMAL
            
            if tipo_izq == TIPO_DATO.ENTERO and tipo_der == TIPO_DATO.CARACTER or tipo_der == TIPO_DATO.ENTERO and tipo_izq == TIPO_DATO.CARACTER:
                return TIPO_DATO.ENTERO
            
            if tipo_izq == TIPO_DATO.DECIMAL and tipo_der == TIPO_DATO.CARACTER or tipo_der == TIPO_DATO.DECIMAL and tipo_izq == TIPO_DATO.CARACTER:
                return TIPO_DATO.DECIMAL
            
            if tipo_izq == TIPO_DATO.CARACTER and tipo_der == TIPO_DATO.CARACTER:
                return TIPO_DATO.ENTERO
            
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Incompatibilidad de tipo en la operación.',self.linea,self.columna))
            return None
            
        if self.tipo == TIPO_OPERACION.MAYOR_QUE or self.tipo == TIPO_OPERACION.MENOR_QUE or self.tipo == TIPO_OPERACION.MAYOR_IGUAL_QUE or self.tipo == TIPO_OPERACION.MENOR_IGUAL_QUE or self.tipo == TIPO_OPERACION.IGUAL_QUE or self.tipo == TIPO_OPERACION.DISTINTO_QUE:
            if (tipo_izq == TIPO_DATO.ENTERO or tipo_izq == TIPO_DATO.DECIMAL or tipo_izq == TIPO_DATO.CARACTER) and (tipo_der == TIPO_DATO.ENTERO or tipo_der == TIPO_DATO.DECIMAL or tipo_der == TIPO_DATO.CARACTER):
                return TIPO_DATO.ENTERO
            
            if (tipo_izq == TIPO_DATO.CADENA or tipo_der == TIPO_DATO.CADENA):
                return TIPO_DATO.ENTERO

            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Incompatibilidad de tipo en la operación.',self.linea,self.columna))
            return None
            
        if self.tipo == TIPO_OPERACION.AND or self.tipo == TIPO_OPERACION.OR or self.tipo == TIPO_OPERACION.BBAND or self.tipo == TIPO_OPERACION.BBOR or self.tipo == TIPO_OPERACION.BBXOR or self.tipo == TIPO_OPERACION.BBIZQ or self.tipo == TIPO_OPERACION.BBDER:
            if (tipo_izq == TIPO_DATO.ENTERO and tipo_der == TIPO_DATO.ENTERO):
                return TIPO_DATO.ENTERO
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Incompatibilidad de tipo en la operación.',self.linea,self.columna))
            return None
        
    def get3D(self,ts) :
        c3d = ""
        if self.tipo == TIPO_OPERACION.ENTERO or self.tipo == TIPO_OPERACION.DECIMAL:
            temporal = ts.getTemporal()
            c3d = temporal + ' = ' + str(self.izquierdo) + ';\n'
        
        elif self.tipo == TIPO_OPERACION.LLAMADA:
            return self.izquierdo.get3D(ts)
        
        elif self.tipo == TIPO_OPERACION.CARACTER:
            temporal = ts.getTemporal()
            c3d = temporal + ' = ' +str(ord(self.izquierdo)) + ';\n'
        
        elif self.tipo == TIPO_OPERACION.CADENA:
            temporal = ts.getTemporal()
            c3d = temporal + ' = \"' +str(self.izquierdo) + '\";\n'
        
        elif self.tipo == TIPO_OPERACION.IDENTIFICADOR:
            var = ts.getSimbolo(self.izquierdo)
            temporal = ts.getTemporal()
            c3d = temporal + ' = ' + var.temporal + ';\n'
        
        elif self.tipo == TIPO_OPERACION.NOT:
            c3d += self.izquierdo.get3D(ts)
            temporal = ts.getTemporal()
            tempizq = ts.getTemporalActual()
            c3d += temporal + ' = !'+tempizq +';\n'

        elif self.tipo == TIPO_OPERACION.BBNOT:
            c3d += self.izquierdo.get3D(ts)
            temporal = ts.getTemporal()
            tempizq = ts.getTemporalActual()
            c3d += temporal + ' = ~'+tempizq +';\n'

        elif self.tipo == TIPO_OPERACION.MENOS_UNARIO:
            c3d += self.izquierdo.get3D(ts)
            temporal = ts.getTemporal()
            tempizq = ts.getTemporalActual()
            c3d += temporal + ' = -'+tempizq +';\n'

        else:
            tizq = self.izquierdo.tipo

            if tizq is None:
                return None

            if not (tizq == TIPO_OPERACION.ENTERO or tizq == TIPO_OPERACION.DECIMAL or tizq == TIPO_OPERACION.IDENTIFICADOR or tizq == TIPO_OPERACION.CARACTER):
                c3d += self.izquierdo.get3D(ts)
                tempizq = ts.getTemporalActual()
            else:
                
                if self.izquierdo.izquierdo is None:
                    return None

                if tizq == TIPO_OPERACION.CARACTER:
                    tempizq = str(ord(self.izquierdo.izquierdo))
                elif tizq == TIPO_OPERACION.IDENTIFICADOR:

                    if ts.getSimbolo(self.izquierdo.izquierdo) is None:
                        return None

                    tempizq = ts.getSimbolo(self.izquierdo.izquierdo).temporal
                else:
                    tempizq = str(self.izquierdo.izquierdo)

            tder = self.derecha.tipo

            if tder is None:
                return None

            if not (tder  == TIPO_OPERACION.ENTERO or tder == TIPO_OPERACION.DECIMAL or tder == TIPO_OPERACION.IDENTIFICADOR or tizq == TIPO_OPERACION.CARACTER):
                c3d += self.derecha.get3D(ts)
                tempder = ts.getTemporalActual()
            else:

                if self.derecha.izquierdo is None:
                    return None

                if tder == TIPO_OPERACION.CARACTER:
                    tempder = str(ord(self.derecha.izquierdo))
                elif tder == TIPO_OPERACION.IDENTIFICADOR:
                    tempder = ts.getSimbolo(self.derecha.izquierdo).temporal
                else:
                    tempder = str(self.derecha.izquierdo)

            temporal = ts.getTemporal()
            c3d += temporal + ' = '+tempizq+ self.signo + tempder+';\n'

        return c3d

    def getAST(self) :
        pass