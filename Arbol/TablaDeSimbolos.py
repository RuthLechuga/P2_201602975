class TablaDeSimbolos() :

    def __init__(self, funciones= {}, simbolos = [], structs = {}) :
        self.simbolos = simbolos
        self.funciones = funciones
        self.structs = structs
        self.temporal = 0
        self.parametro = 0
        self.retorno = 0
        self.pila = 0
        self.label = 0
        self.ambito = 'global'
        self.padre = None
        self.et_salida = []
        self.et_inicio = []

    def addSimbolo(self, simbolo):
        for s in self.simbolos:
            if simbolo.identificador == s.identificador and simbolo.ambito == s.ambito:
                return False

        self.simbolos.append(simbolo)
        return True
    
    def getSimbolo(self, identificador):
        for simbolo in self.simbolos:
            if simbolo.identificador == identificador and (simbolo.ambito == self.ambito or simbolo.ambito=='global'):
                return simbolo

        return None
    
    def addFuncion(self, funcion):
        if funcion.identificador in self.funciones:
            return False

        self.funciones[funcion.identificador] = funcion
        return True

    def getFuncion(self, identificador):
        if not identificador in self.funciones:
            return None

        return self.funciones[identificador]
    
    def addStruct(self, struct):
        if struct.identificador in self.structs:
            return False

        self.structs[struct.identificador] = struct
        return True

    def getStruct(self, identificador):
        if not identificador in self.structs:
            return None

        return self.structs[identificador]
    
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
    
    def getLabel(self):
        self.label += 1
        return "Label_"+str(self.label)
    
    def getLabelActual(self):
        return "Label_"+str(self.label)
        
    def reiniciar(self):
        self.simbolos.clear()
        self.funciones.clear()
        self.temporal = 0
        self.parametro = 0
        self.retorno = 0
        self.pila = 0
        self.ambito = 'global'