from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class DeclaracionStruct(Instruccion) :

    def __init__(self,tipo,identificador,accesos,linea,columna) :
        self.tipo = tipo
        self.identificador = identificador
        self.accesos = accesos
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :

        struct = ts.getStruct(self.tipo)

        if struct is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El struct '+self.tipo+' no ha sido declarado.',self.linea,self.columna))
            return

        dimensiones = 1;
        if not self.accesos is None:
            dimensiones = len(self.accesos)
        
        if not ts.addSimbolo(Simbolo(self.identificador,TIPO_DATO.STRUCT,dimensiones,self.linea,self.columna,ts.ambito)):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador '+self.identificador+' ya existe.',self.linea,self.columna))
            

    def get3D(self,ts) :
        var = ts.getSimbolo(self.identificador)
        temporal = ts.getTemporal()
        var.temporal = temporal
        c3d = temporal +'= array();\n'
        return c3d

    def getAST(self) :
        ast = "\""+str(self)+"\" [label=\"ins_declaracion_struct\"] ;\n"

        ast += "\""+str(self)+"_struct\" [label=\"STRCUCT\"] ;\n"
        ast += "\""+str(self)+"\" -> \""+str(self)+"_struct\"\n"

        ast += "\""+str(self)+self.tipo+"\" [label=\"TIPO\"] ;\n"
        ast += "\""+str(self)+"\" -> \""+str(self)+self.tipo+"\"\n"

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

        return ast
