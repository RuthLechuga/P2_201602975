class TablaDeSimbolos() :

    def __init__(self, funciones= {}, simbolos = {}) :
        self.simbolos = simbolos
        self.funciones = funciones
        self.temporal = 0
        self.parametro = 0
        self.retorno = 0
        self.pila = 0
        self.ambito = 'global'
        self.padre = None

    def addSimbolo(self, simbolo):
        if simbolo.identificador in self.simbolos:
            return False

        self.simbolos[simbolo.identificador] = simbolo
        return True
    
    def getSimbolo(self, identificador):
        if not identificador in self.simbolos:
            return None

        return self.simbolos[identificador]
    
    def addFuncion(self, funcion):
        self.funciones[funcion.identificador] = funcion
    
    def getFuncion(self, identificador):
        if not identificador in self.funciones:
            return None

        return self.funciones[identificador]
    
    def getTemporal(self):
        self.temporal += 1
        return "$t"+ str(self.temporal)
    
    def getTemporalActual(self):
        return "$t"+str(self.temporal)
    
    def getParametro(self):
        self.parametro += 1
        return "$a"+str(self.parametro)
    
    def getParametroActual(self):
        return "$a"+str(self.parametro)
    
    def getRetorno(self):
        self.retorno += 1
        return "$v"+str(self.retorno)
    
    def getRetornoActual(self):
        return "$v"+str(self.retorno)
    
    def getPila(self):
        self.pila += 1
        return "$s"+str(self.pila)
    
    def getPilaActual(self):
        return "$s"+str(self.pila)
    
    def reiniciar(self):
        self.simbolos.clear()
        self.funciones.clear()
        self.temporal = 0
        self.parametro = 0
        self.retorno = 0
        self.pila = 0
        self.ambito = 'global'