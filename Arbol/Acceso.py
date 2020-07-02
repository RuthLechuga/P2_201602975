from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Acceso(Instruccion) :

    def __init__(self,identificador,accesos,linea,columna) :
        self.identificador = identificador
        self.accesos = accesos
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        return TIPO_DATO.ENTERO

    def get3D(self,ts) :
        c3d = '' 
        temporal_id = ts.getSimbolo(self.identificador).temporal
        cad_accesos = ''

        for acceso in self.accesos:
            if isinstance(acceso,str):
                cad_accesos += '[\''+acceso+'\']'
            else:
                c3d += acceso.get3D(ts)
                t = ts.getTemporalActual()
                cad_accesos += '['+t+']'
        
        temporal = ts.getTemporal()
        c3d += temporal + '= '+temporal_id+cad_accesos+';\n'

        return c3d

    def getAST(self) :
        ast =   "\""+str(self)+"\" [label=\"ACCESOS\"] ;\n" +\
                "   \""+str(self)+"et"+"\" [label=\""+self.identificador+"\"] ;\n" +\
                "   \""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"
        
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
