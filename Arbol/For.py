from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class For(Instruccion) :

    def __init__(self, declaracion, condicion, incremento, instrucciones, linea, columna) :
        self.declaracion = declaracion
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        if (not isinstance(self.declaracion,str)) and (not self.declaracion is None):
            self.declaracion.analizar(ts,mensajes)

        if not self.condicion is None:
            self.condicion.analizar(ts,mensajes)

        if not self.incremento is None:
            self.incremento.analizar(ts,mensajes)
        
        for instruccion in self.instrucciones:
            instruccion.analizar(ts,mensajes)

    def get3D(self,ts) :
        c3d = ''
        label_inc = ts.getLabel()
        label_cuerpo = ts.getLabel()
        label_salida = ts.getLabel()

        ts.et_salida.append(label_salida)
        ts.et_inicio.append(label_inc)

        c3d = '#inicializacion for:\n'
        c3d += self.declaracion.get3D(ts)
        c3d += 'goto '+label_cuerpo+';\n';

        c3d += label_inc +':  #incremento del for:\n'
        c3d += self.incremento.get3D(ts)

        c3d += label_cuerpo +':  #for \n'

        c3d += self.condicion.get3D(ts)
        et_expresion = ts.getTemporalActual()
        et_not_expresion = ts.getTemporal()
        c3d += et_not_expresion + ' = !'+et_expresion+';\n'

        c3d += 'if ('+et_not_expresion+') goto '+label_salida+';\n'

        for instruccion in self.instrucciones:
            c3d += instruccion.get3D(ts)
        c3d += 'goto '+label_inc+';\n\n'

        c3d += label_salida +':   #salida for \n'

        ts.et_inicio.pop()
        ts.et_salida.pop()

        return c3d

    def getAST(self) :
        ast = "   \""+str(self)+"\" [label=\"ins_for\"] ;\n" +\
        "   \""+str(self)+"for"+"\" [label=\"for\"] ;\n" +\
        "   \""+str(self)+"\" -> \""+str(self)+"for"+"\"\n"

        ast+= "   \""+str(self.declaracion)+"\" [label=\"DECLARACION\"] ;\n";
        ast+= self.declaracion.getAST()
        ast+= "   \""+str(self)+"\" -> \""+str(self.declaracion)+"\"\n";

        ast+= "   \""+str(self.condicion)+"\" [label=\"CONDICION\"] ;\n";
        ast+= self.condicion.getAST()
        ast+= "   \""+str(self)+"\" -> \""+str(self.condicion)+"\"\n";        

        ast+= "   \""+str(self.incremento)+"\" [label=\"INCREMENTO\"] ;\n";
        ast+= self.incremento.getAST()
        ast+= "   \""+str(self)+"\" -> \""+str(self.incremento)+"\"\n"; 

        ast += "\""+str(self.instrucciones)+"\" [label=\"instrucciones\"] ;\n"
        ast += "\""+str(self)+"\" -> \""+str(self.instrucciones)+"\"\n"
        
        for instruccion in self.instrucciones:
            ast += "\""+str(instruccion)+"\" [label=\"instruccion\"] ;\n"
            ast += "\""+str(self.instrucciones)+"\" -> \""+str(instruccion)+"\"\n"
            ast += instruccion.getAST()
               
        return ast