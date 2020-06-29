from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Scanf import *

class Declaracion(Instruccion) :

    def __init__(self, tipo, identificador, accesos, expresion, linea, columna) :
        self.tipo = tipo
        self.identificador = identificador
        self.accesos = accesos
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        self.tipo_expresion = None
    
    def analizar(self,ts,mensajes) :

        if self.accesos is None and self.expresion is None:
            if not ts.addSimbolo(Simbolo(self.identificador,self.tipo,1,self.linea,self.columna,ts.ambito)):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador '+self.identificador+' ya existe.',self.linea,self.columna))
            return
        
        if self.accesos is None and (not self.expresion is None):
            
            if isinstance(self.expresion,Scanf):
                tipo = self.tipo
            else:
                tipo = self.expresion.analizar(ts,mensajes)
            
            self.tipo_expresion = tipo

            if tipo is None:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Expresión inválida para:'+self.identificador+'.',self.linea,self.columna))
            
            if isinstance(tipo,Mensaje):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Expresión inválida para:'+self.identificador+'.',self.linea,self.columna))
    
            elif not tipo == self.tipo and not(tipo == TIPO_DATO.CARACTER and self.tipo == TIPO_DATO.ENTERO) and not(tipo == TIPO_DATO.ENTERO and self.tipo == TIPO_DATO.CARACTER) and not(tipo == TIPO_DATO.ENTERO and self.tipo == TIPO_DATO.DECIMAL): 
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión no coincide con el tipo de dato de:'+self.identificador,self.linea,self.columna))
            
            if not ts.addSimbolo(Simbolo(self.identificador,self.tipo,1,self.linea,self.columna,ts.ambito)):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador '+self.identificador+' ya existe.',self.linea,self.columna))
            
            return

    def get3D(self,ts):
        c3d = ""

        var = ts.getSimbolo(self.identificador)

        if self.accesos is None and self.expresion is None:
            temporal = ts.getTemporal()
            var.temporal = temporal
            if self.tipo == TIPO_DATO.ENTERO:
                c3d = temporal + " = 0;\n"

            elif self.tipo == TIPO_DATO.DECIMAL:
                c3d = temporal + " = 0.0;\n"
            
            elif self.tipo == TIPO_DATO.CARACTER:
                c3d = temporal + " = \"\";\n"
        
        if self.accesos is None and (not self.expresion is None):

            if isinstance(self.expresion,Scanf):
                temporal = ts.getTemporal()
                c3d += temporal + ' = read();\n'
                var.temporal = temporal

            elif self.tipo == self.tipo_expresion or self.tipo == TIPO_DATO.DECIMAL and self.tipo_expresion == TIPO_DATO.ENTERO:
                c3d = self.expresion.get3D(ts)
                var.temporal = ts.getTemporalActual()
            else:
                if self.tipo == TIPO_DATO.CARACTER and self.tipo_expresion == TIPO_DATO.ENTERO:
                    c3d = self.expresion.get3D(ts);
                    temp_actual = ts.getTemporalActual()
                    temporal = ts.getTemporal()
                    c3d += temporal + ' = (char)'+temp_actual+';\n'
                    var.temporal = temporal
                
                elif self.tipo == TIPO_DATO.ENTERO and self.tipo_expresion == TIPO_DATO.CARACTER:
                    c3d = self.expresion.get3D(ts);
                    temp_actual = ts.getTemporalActual()
                    temporal = ts.getTemporal()
                    c3d += temporal + ' = (int)'+temp_actual+';\n'
                    var.temporal = temporal
        return c3d; 
    
    def getAST(self):
        pass