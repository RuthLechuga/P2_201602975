from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Ternario(Instruccion) :

    def __init__(self,condicion,expresion_true,expresion_false,linea,columna) :
        self.condicion = condicion
        self.expresion_true = expresion_true
        self.expresion_false = expresion_false
        self.linea = linea
        self.columna = columna

    def analizar(self,ts,mensajes) :
        self.condicion.analizar(ts,mensajes)
        self.expresion_true.analizar(ts,mensajes)
        self.expresion_false.analizar(ts,mensajes)
        return TIPO_DATO.ENTERO

    def get3D(self,ts) :
        c3d = self.condicion.get3D(ts)
        cond_temp = ts.getTemporalActual()
        
        c3d += self.expresion_true.get3D(ts)
        true_temp = ts.getTemporalActual()

        c3d += self.expresion_false.get3D(ts)
        false_temp = ts.getTemporalActual()

        true_label = ts.getLabel()
        false_label = ts.getLabel()
        salida_label = ts.getLabel()

        temp_resultado = ts.getTemporal()
        c3d += 'if('+cond_temp+') goto '+ true_label+'  ;\n'
        c3d += 'if(!'+cond_temp+') goto '+ false_label+' ;\n'

        c3d += true_label +':\n'
        c3d += temp_resultado +'='+true_temp+';\n'
        c3d += 'goto '+salida_label+';\n'

        c3d += false_label +':\n'
        c3d += temp_resultado +'='+false_temp+';\n'

        c3d += salida_label+':\n'
        return c3d

    def getAST(self) :
        ast = "\""+str(self)+"\" [label=\"operador_ternario\"] ;\n";
        
        ast+= self.condicion.getAST();
        ast+= "   \""+str(self)+"\" -> \""+str(self.condicion)+"\"\n";
        
        ast+="   \""+str(self)+"q\" [label=\"?\"] ;\n";
        ast+= "   \""+str(self)+"\" -> \""+str(self)+"q\"\n";
        
        ast+= self.expresion_true.getAST();
        ast+= "   \""+str(self)+"\" -> \""+str(self.expresion_true)+"\"\n";
        
        ast+="   \""+str(self)+"dp\" [label=\":\"] ;\n";
        ast+= "   \""+str(self)+"\" -> \""+str(self)+"dp\"\n";
        
        ast+= self.expresion_false.getAST();
        ast+= "   \""+str(self)+"\" -> \""+str(self.expresion_false)+"\"\n";
        
        return ast;
