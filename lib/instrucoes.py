# -*- encoding: UTF-8 -*-

class Instrucao_R_I (object):
    def __init__(self, tipo,  resultado, valor1, valor2=None, func=None):
        self.__tipo = tipo
        self.__resultado = resultado
        self.__valor1 = valor1
        self.__valor2 = valor2
        self.__func = func
        
    def getTipo (self):
        return self.__tipo
    def getResultado (self):
        return self.__resultado
    def setResultado (self, valor):
        self.__resultado = valor
    def getValor1 (self):
        return self.__valor1
    def getValor2 (self):
        return self.__valor2
    def __str__(self):
        if self.__valor2:
            return "%s %s,%s,%s" % (self.__tipo, self.__resultado, self.__valor1, self.__valor2)
        else:
            return "%s %s,%s" % (self.__tipo, self.__resultado, self.__valor1)

class Instrucao_J (object):
    def __init__(self,tipo, endereco):
        self.__tipo = tipo
        self.__endereco = endereco
        
    def getTipo (self):
        return self.__tipo
    def getEndereco (self):
        return self.endereco
    def __str__(self):
        return "%s %s" % (self.__tipo, self.__endereco)