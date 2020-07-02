from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *
from .Scanf import *
from .Expresion import *

class Declaracion(Instruccion) :

    def __init__(self, tipo, identificador, accesos, expresion, linea, columna, isParametro = False) :
        self.tipo = tipo
        self.identificador = identificador
        self.accesos = accesos
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        self.tipo_expresion = None
        self.isParametro = isParametro
    
    def analizar(self,ts,mensajes) :

        if self.expresion is None:
            dimension = 1
            if not self.accesos is None:
                dimension = len(self.accesos)
            
            if not ts.addSimbolo(Simbolo(self.identificador,self.tipo,dimension,self.linea,self.columna,ts.ambito)):
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
        
        else:
            if not isinstance(self.expresion,list) and not isinstance(self.expresion,Expresion):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresion del identificador '+self.identificador+' no es correcta para un arreglo.',self.linea,self.columna))
            
            if not ts.addSimbolo(Simbolo(self.identificador,self.tipo,len(self.accesos),self.linea,self.columna,ts.ambito)):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador '+self.identificador+' ya existe.',self.linea,self.columna))
            return

    def get3D(self,ts):
        c3d = ""

        var = ts.getSimbolo(self.identificador)

        if self.isParametro:
            var.temporal = ts.getParametro()
            return c3d

        elif self.accesos is None and self.expresion is None:
            temporal = ts.getTemporal()
            var.temporal = temporal
            if self.tipo == TIPO_DATO.ENTERO:
                c3d = temporal + " = 0;\n"

            elif self.tipo == TIPO_DATO.DECIMAL:
                c3d = temporal + " = 0.0;\n"
            
            elif self.tipo == TIPO_DATO.CARACTER:
                c3d = temporal + " = \"\";\n"
        
        elif self.accesos is None and (not self.expresion is None):

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
        
        elif (not self.accesos is None) and self.expresion is None:
            temporal = ts.getTemporal()
            var.temporal = temporal
            c3d = temporal + " = array();\n"
        
        elif (not self.accesos is None) and (not self.expresion is None):
            temporal = ts.getTemporal()
            var.temporal = temporal
            c3d = temporal + " = array();\n"

            #arreglos de una dimension
            if len(self.accesos) == 1:
                pos = 0
                if isinstance(self.expresion,list):
                    for item in self.expresion:
                            c3d += item.get3D(ts)
                            c3d += temporal+'['+str(pos)+'] = '+ ts.getTemporalActual()+';\n'
                            pos += 1
                else:
                    c3d += self.expresion.get3D(ts)
                    c3d += temporal + '='+ts.getTemporalActual()+';\n'

            #arreglos de dos dimensiones
            elif len(self.accesos) == 2:
                max_i = len(self.expresion)
                max_j = len(self.expresion[0])

                for i in range(max_i):
                    for j in range(max_j):
                        c3d += self.expresion[i][j].get3D(ts)
                        c3d += temporal+'['+str(i)+']['+str(j)+'] ='+ts.getTemporalActual()+';\n'
            
            #arreglos de tres dimensiones
            elif len(self.accesos) == 3:
                max_i = len(self.expresion)
                max_j = len(self.expresion[0])
                max_k = len(self.expresion[0][0])

                for i in range(max_i):
                    for j in range(max_j):
                        for k in range(max_k):
                            c3d += self.expresion[i][j][k].get3D(ts)
                            c3d += temporal+'['+str(i)+']['+str(j)+']['+str(k)+'] ='+ts.getTemporalActual()+';\n'

            #arreglos de cuatro dimensiones
            elif len(self.accesos) == 4:
                max_i = len(self.expresion)
                max_j = len(self.expresion[0])
                max_k = len(self.expresion[0][0])
                max_z = len(self.expresion[0][0][0])

                for i in range(max_i):
                    for j in range(max_j):
                        for k in range(max_k):
                            for z in range(max_z):
                                c3d += self.expresion[i][j][k][z].get3D(ts)
                                c3d += temporal+'['+str(i)+']['+str(j)+']['+str(k)+']['+str(z)+'] ='+ts.getTemporalActual()+';\n'

        return c3d; 
    
    def getAST(self):
        ast = "\""+str(self)+"\" [label=\"ins_declaracion\"] ;\n"
        ast += "\""+str(self)+self.identificador+"\" [label=\"IDENTIFICADOR\"] ;\n"
        ast += "\""+str(self)+"\" -> \""+str(self)+self.identificador+"\"\n"

        if not self.accesos is None:
            ast += "\""+str(self.accesos)+"\" [label=\"accesos\"] ;\n";
            ast += "\""+str(self)+"\" -> \""+str(self.accesos)+"\"\n";
            for acceso in self.accesos:
                if not isinstance(acceso,str):
                    ast += "\""+str(acceso)+"\" [label=\"acceso\"] ;\n";
                    ast += "\""+str(self.accesos)+"\" -> \""+str(acceso)+"\"\n";
                    ast += acceso.getAST();
                else:
                    ast += "\""+str(self)+str(acceso)+"\" [label=\"cadena\"] ;\n";
                    ast += "\""+str(self.accesos)+"\" -> \""+str(self)+str(acceso)+"\"\n";

        if not self.expresion is None:
            ast += "\""+str(self)+"igual\" [label=\"=\"] ;\n"
            ast += "\""+str(self)+"\" -> \""+str(self)+"igual\"\n"
            ast += "\""+str(self)+"\" -> \""+str(self.expresion)+"\"\n";
            if not isinstance(self.expresion,list):
                ast += self.expresion.getAST()
            else:
                ast += "\""+str(self.expresion)+"\" [label=\"lista\"] ;\n";
                    
        return ast