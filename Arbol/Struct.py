from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Struct(Instruccion) :

    def __init__(self,identificador,atributos,linea,columna) :
        self.identificador = identificador
        self.atributos = atributos
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        ambito_actual = ts.ambito
        
        #valida que la función no exista en el contexto actual
        if not ts.addStruct(self):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La definición del struct: '+ self.identificador+ ' ya existe.',self.linea,self.columna))
            return
        
        ts.ambito = 'struct_'+self.identificador
        for atributo in self.atributos:
            atributo.analizar(ts,mensajes)

        ts.ambito = ambito_actual

    def get3D(self,ts) :
        c3d = ''
        return c3d

    def getAST(self) :
        ast = "\""+str(self)+"\" [label=\"ins_definicion_struct\"] ;\n"

        ast += "\""+str(self)+self.identificador+"\" [label=\"IDENTIFICADOR\"] ;\n"
        ast += "\""+str(self)+"\" -> \""+str(self)+self.identificador+"\"\n"
    
        ast += "\""+str(self.atributos)+"\" [label=\"atributos\"] ;\n";
        ast += "\""+str(self)+"\" -> \""+str(self.atributos)+"\"\n";
            
        for atributo in self.atributos:
            ast += "\""+str(atributo)+"\" [label=\"atributo\"] ;\n";
            ast += "\""+str(self.atributos)+"\" -> \""+str(atributo)+"\"\n";
            ast += atributo.getAST();

        return ast
