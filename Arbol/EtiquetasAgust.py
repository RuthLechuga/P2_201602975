from .Instruccion import Instruccion

class EtiquetasAgust(Instruccion) :

    def __init__(self, codigo) :
        self.codigo = codigo

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        return self.codigo

    def getAST(self) :
        ast = "\""+str(self)+"\" [label=\"ins_et_augus\"] ;\n" +\
            "\""+str(self)+"et"+"\" [label=\""+str(codigo)+"\"] ;\n" +\
            "\""+str(self)+"\" -> \""+str(self)+"et"+"\"\n"
 
        return ast
