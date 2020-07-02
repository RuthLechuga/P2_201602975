from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Elseif(Instruccion) :

    def __init__(self, condicion, instrucciones, linea, columna) :
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :

        if not self.condicion is None:
            self.condicion.analizar(ts,mensajes)
        
        for instruccion in self.instrucciones:
            instruccion.analizar(ts,mensajes)

    def get3D(self,ts) :
        c3d = ''

        for instruccion in self.instrucciones:
            c3d += instruccion.get3D(ts)
        
        if not self.condicion is None:
            et_falsa = ts.getLabel()
            cod_cond = self.condicion.get3D(ts)
            et_cond = ts.getTemporalActual()
            et_not = ts.getTemporal()
            cod_cond += et_not + ' = !'+et_cond+';\n'
            cod_cond += 'if ('+et_not+') goto '+et_falsa+';\n'
            c3d = cod_cond+c3d

        return c3d

    def getAST(self) :
        ast = ''

        if not self.condicion is None:
            ast += "\""+str(self)+"\" [label=\"ins_if\"] ;\n" +\
                "\""+str(self)+"et"+"\" [label=\"if\"] ;\n" +\
                "\""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"
            ast += "\""+str(self.condicion)+"\" [label=\"expresion\"] ;\n" +\
                "\""+str(self)+"\" -> \""+str(self.condicion)+"\"\n"
        else:
            ast += "\""+str(self)+"\" [label=\"ins_else\"] ;\n" +\
                "\""+str(self)+"et"+"\" [label=\"else\"] ;\n" +\
                "\""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"
        
        ast += "\""+str(self.instrucciones)+"\" [label=\"instrucciones\"] ;\n";
        ast += "\""+str(self)+"\" -> \""+str(self.instrucciones)+"\"\n";

        for instruccion in self.instrucciones:
            ast += "\""+str(instruccion)+"\" [label=\"instruccion\"] ;\n";
            ast += "\""+str(self.instrucciones)+"\" -> \""+str(instruccion)+"\"\n";
            ast += instruccion.getAST();

        return ast