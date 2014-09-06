# -*- encoding: UTF-8 -*-

class ULA (object):
    def __init__(self):
        self.__operacao = None
        self.__valor1 = 0
        self.__valor2 = 0
        self.__zero = 0
        self.__resultado = 0
        
    def opera (self, UC, instrucao, valores):
        if UC.getALUOp() == '00':
            if not valores[2]:
                valores[0].setValor(valores[1])
                self.__resultado = valores[0].getValor()
                self.__operacao = '010'
                self.__valor1 = valores[1]
            else:
                valores[0].setValor( int(valores[1]) + int(valores[2]) )
                self.__resultado = valores[0].getValor()
                self.__operacao = '010'
                self.__valor1 = valores[1]
                self.__valor2 = valores[2]
        elif UC.getALUOp() == '10':
            if instrucao.getTipo() in ['addi','add','addu','addiu']:
                valores[0].setValor(int(valores[1])+int(valores[2]))
                self.__resultado = valores[0].getValor()
                self.__operacao = '010'
                self.__valor1 = valores[1]
                self.__valor2 = valores[2]
            elif instrucao.getTipo() in ['sub','subu']:
                valores[0].setValor(int(valores[1])-int(valores[2]))
                self.__resultado = valores[0].getValor()
                self.__operacao = '110'
                self.__valor1 = valores[1]
                self.__valor2 = valores[2]
            elif instrucao.getTipo() in ['slt','slti']:
                valores[0].setValor( int( int(valores[1]) < int(valores[2]) ))
                self.__resultado = valores[0].getValor()
                self.__operacao = '111'
                self.__valor1 = valores[1]
                self.__valor2 = valores[2]
            elif instrucao.getTipo() in ['and', 'andi', 'andiu', 'andu']:
                valores[0].setValor( int( int(valores[1]) and int(valores[2]) ) )
                self.__resultado = valores[0].getValor()
                self.__operacao = '000'
                self.__valor1 = valores[1]
                self.__valor2 = valores[2]
            elif instrucao.getTipo() in ['or', 'ori', 'oriu', 'oru']:
                valores[0].setValor( int( int(valores[1]) or int(valores[2]) ))
                self.__resultado = valores[0].getValor()
                self.__operacao = '000'
                self.__valor1 = valores[1]
                self.__valor2 = valores[2]
                
    def getOperacao (self):
        return self.__operacao
    def setOperacao (self, op):
        self.__operacao = op
    def getValor1 (self):
        return self.__valor1
    def setValor1 (self, valor1):
        self.__valor1 = valor1
    def getValor2 (self):
        return self.__valor2
    def setValor2 (self, valor2):
        self.__valor2 = valor2
    def getResultado (self):
        return self.__resultado
    def setResultado (self, resultado):
        self.__resultado = resultado