from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Scanf import *

class Asignacion(Instruccion) :

    def __init__(self, identificador, accesos, signo, expresion, linea, columna) :
        self.identificador = identificador
        self.accesos = accesos
        self.signo = signo
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        self.temporal = ''
        self.isParametro = False

    def analizar(self,ts,mensajes) :
        simbolo = ts.getSimbolo(self.identificador)

        if simbolo is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La variables: '+ self.identificador+ ' no existe.',self.linea,self.columna))
            return
        
        if isinstance(self.expresion,Scanf):
            return
        
        if not self.accesos is None:
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
        self.temporal = temporal

        if isinstance(self.expresion,Scanf):
            c3d = temporal + ' = read();\n'
            return c3d

        c3d = self.expresion.get3D(ts)
        resultado = ts.getTemporalActual()

        if self.isParametro:
            return c3d
        
        if not self.accesos is None:
            cad_accesos = ''
            for acceso in self.accesos:
                if isinstance(acceso,str):
                    cad_accesos += '[\''+acceso+'\']'
                else:
                    c3d += acceso.get3D(ts)
                    t = ts.getTemporalActual()
                    cad_accesos += '['+t+']'
            c3d += temporal + cad_accesos + ' = '+resultado+';\n'
            return c3d
            
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