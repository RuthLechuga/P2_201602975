from .Instruccion import Instruccion

class EtiquetasAgust(Instruccion) :

    def __init__(self, codigo) :
        self.codigo = codigo

    def analizar(self,ts,mensajes) :
        pass

    def get3D(self,ts) :
        return self.codigo

    def getAST(self) :
        pass
