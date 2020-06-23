import abc 
class Instruccion(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def analizar(self,ts,mensajes) :
        pass
    
    @abc.abstractmethod
    def get3D(self,ts) :
        pass
    
    @abc.abstractmethod
    def getAST(self) :
        pass