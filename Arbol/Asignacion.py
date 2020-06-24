from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Asignacion(Instruccion) :

    def __init__(self, identificador, accesos, signo, expresion, linea, columna) :
        self.identificador = identificador
        self.accesos = accesos
        self.signo = signo
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        simbolo = ts.getSimbolo(self.identificador)

        if simbolo is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La variables: '+ self.identificador+ ' no existe.',self.linea,self.columna))
            return
        
        tipo = self.expresion.analizar(ts,mensajes)

        if tipo is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Expresión inválida para:'+self.identificador+'.',self.linea,self.columna))
        
        if isinstance(tipo,Mensaje):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Expresión inválida para:'+self.identificador+'.',self.linea,self.columna))

        elif not tipo == simbolo.tipo and not(tipo == TIPO_DATO.CARACTER and simbolo.tipo == TIPO_DATO.ENTERO) and not(tipo == TIPO_DATO.ENTERO and simbolo.tipo == TIPO_DATO.CARACTER) and not(tipo == TIPO_DATO.ENTERO and simbolo.tipo == TIPO_DATO.DECIMAL): 
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión no coincide con el tipo de dato de:'+self.identificador,self.linea,self.columna))

    def get3D(self,ts):
        temporal = ts.getSimbolo(self.identificador).temporal
        
        c3d = self.expresion.get3D(ts)
        resultado = ts.getTemporalActual()

        if self.signo == '=':
            c3d += temporal + ' = ' + resultado + ';\n'
        
        elif self.signo == '+=':
            c3d += temporal + ' = ' + temporal + '+' + resultado + ';\n'
        
        elif self.signo == '-=':
            c3d += temporal + ' = ' + temporal + '-' + resultado + ';\n'
        
        elif self.signo == '/=':
            c3d += temporal + ' = ' + temporal + '/' + resultado + ';\n'
        
        elif self.signo == '*=':
            c3d += temporal + ' = ' + temporal + '*' + resultado + ';\n'
        
        elif self.signo == '%=':
            c3d += temporal + ' = ' + temporal + '%' + resultado + ';\n'
        
        elif self.signo == '&=':
            c3d += temporal + ' = ' + temporal + '&' + resultado + ';\n'
        
        elif self.signo == '<<=':
            c3d += temporal + ' = ' + temporal + '<<' + resultado + ';\n'
        
        elif self.signo == '>>=':
            c3d += temporal + ' = ' + temporal + '>>' + resultado + ';\n'
        
        elif self.signo == '|=':
            c3d += temporal + ' = ' + temporal + '|' + resultado + ';\n'
        
        elif self.signo == '^=':
            c3d += temporal + ' = ' + temporal + '^' + resultado + ';\n'
        return c3d; 
    
    def getAST(self):
        pass