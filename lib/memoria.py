# -*- encoding: UTF-8 -*-

class Variavel (object):
    def __init__ (self, nome, tipo=".word", valor="---"):
        self.__nome = nome
        self.__valor = valor
        self.__tipo = tipo
        self.__endereco = 268435456
        self.__enderecoFim = self.__endereco
        self.setEndereco()
    def getNome (self):
        return self.__nome
    def getValor (self):
        return self.__valor
    def setValor (self, valor):
        self.__valor = valor
    def setEndereco (self, valor=268435456):
        if valor < 2147483647:
            self.__endereco = valor
            self.setEnderecoFim()
        else:
            raise Exception("Memória Cheia!")
    def getEndereco (self):
        return self.__endereco
    def setEnderecoFim (self):
        if self.__tipo == ".half":
            self.__enderecoFim = self.__endereco + 2
        elif self.__tipo == ".byte":
            self.__enderecoFim = self.__endereco + 1
        else:
            self.__enderecoFim = self.__endereco + 4
    def getEnderecoFim (self):
        return self.__enderecoFim

class Mem_dados (object):
    def __init__(self):
        self.__dados = []
    def getDados (self):
        return self.__dados
    def setDado (self, variavel):
        if len(self.__dados) > 0:
            ultimo = self.__dados[len(self.__dados)-1]
            end = ultimo.getEnderecoFim() + 1
            variavel.setEndereco(end)
        self.__dados.append(variavel)
    def getDado (self, nome):
        try:
            for variavel in self.__dados:
                print variavel.getNome()
                if (variavel.getNome()[:len(variavel.getNome())-1] == nome):
                    return variavel
            return None
        except:
            raise Exception("Parâmetros inválidos")
    def store_word (self, reg, var):
        try:
            for variavel in self.dados:
                if (variavel.getNome() == var):
                    variavel.setValor(reg.getValor())
                    return True
            return False
        except:
            raise Exception("Parâmetros inválidos")
        
class Mem_instrucoes (object):
    def __init__(self):
        self.__dados = []
    def getDados (self):
        return self.__dados
    def setDado (self, inst):
        self.__dados.append(inst)
    def setCursor (self, indice):
        self.__cursor = indice
    def getInstrucao (self, pc):
        return self.__dados[pc]