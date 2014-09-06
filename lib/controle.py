# -*- encoding: UTF-8 -*-
from lib.instrucoes import Instrucao_R_I, Instrucao_J
import re

class UC(object):
    def __init__(self):
        self.__ALUfonte = 0
        self.__ALUop = 0
        self.__escreveReg = 0
        self.__escreveDados = 0
        self.__memToReg = 0
        self.__lerDados = 0
        self.__regDestino = 0
        self.__desvioCondicional = 0
        self.__desvioIncondicional = 0
        
    def configura (self, instrucao):
        R = r'(add[i|u|iu])|(add)|(subu)|(sub)|(mult)|(div)|(andi)|(and)|(ori)|(or)|(xor)|(nor)|(slti)|(slt)'
        I = r'(li)|(lw)|(lhu)|(lh)|(lbu)|(lb)|(sw)|(sh)|(sb)|(lui)|(beq)|(bne)'
        J = r'(jal)|(jr)|(j)'
        self.__init__()
        tipo = instrucao.getTipo()
        if type(instrucao) is Instrucao_R_I and re.match(R, tipo):
            self.__ALUop = '10'
            self.__escreveReg = 1
            if tipo == "addi" or tipo == "addiu":
                self.__ALUfonte = 1
        elif type(instrucao) is Instrucao_R_I and re.match(I, tipo):
            self.__ALUop = '00'
            self.__ALUfonte = 1
            if tipo == "bne" or tipo == "beq" or tipo == 'slt':
                self.__ALUop = '01'
                self.__lerDados = 1
                self.__desvioCondicional = 1
            elif tipo == 'sw':
                self.__escreveDados = 1
            elif tipo == 'lw':
                self.__lerDados = 1
                self.__memToReg = 1
                self.__escreveReg = 1
            elif tipo == 'li':
                self.__regDestino = 1
                self.__escreveReg = 1
        elif type(instrucao) is Instrucao_J and re.match(J, tipo):
            self.__desvioIncondicional = 1

    def decodifica (self, instrucao):
        if type(instrucao) is str:
            return
        self.configura(instrucao)
    
    def getRegDestino (self):
        return self.__regDestino
    def getDesvioCondicional (self):
        return self.__desvioCondicional
    def getLerDados (self):
        return self.__lerDados
    def getEscreveDados (self):
        return self.__escreveDados
    def getALUOp (self):
        return self.__ALUop
    def getMemToReg (self):
        return self.__memToReg
    def getALUFonte (self):
        return self.__ALUfonte
    def getEscreveReg (self):
        return self.__escreveReg