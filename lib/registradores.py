# -*- encoding: UTF-8 -*-

class Registrador(object):
    def __init__(self, valor, reservado=False):
        self.__valor = valor
        self.__reservado = reservado
        self.__nome = ""

    def getValor (self):
        return self.__valor
    def setValor (self, novoValor, system=False):
        if not self.__reservado or system == True:
            self.__valor = novoValor
    def getNome (self):
        return self.__nome
    def setNome (self, novoNome, reservado=False):
        self.__nome = novoNome
        self.__reservado = reservado
        if reservado:
            self.__valor = "Reservado pelo sistema"
    def __str__ (self):
        return self.__nome
        
class Banco (object):
    def __init__(self):
        self.__registradores = []
        self.__criaBanco()
        self.__criaNomes()
    
    def __criaBanco (self):
        for i in range(34):
            # Inicializa todos os __registradores com 0
            reg = Registrador(0)
            self.__registradores.append(reg)

    def __criaNomes(self):
        # Constante $0 ou $zero
        self.__registradores[0].setNome('$zero')
        self.__registradores[0].setValor(0)
        # Assembler Temporary
        self.__registradores[1].setNome('$at', True)
        # Resultados de função e expressões de avaliação
        self.__registradores[2].setNome('$v0')
        self.__registradores[3].setNome('$v1')
        # Primeiros quatro parâmetros para subrotinas (arguments)
        for i in range(4, 8):
            self.__registradores[i].setNome('$a%d'% i)
        #__registradores temporários e valores salvos
        for i in range(8, 26):
            if i not in range(16, 24) and i < 23:
                self.__registradores[i].setNome("$t%d"%(i-8))
            elif i > 23:
                self.__registradores[i].setNome("$t%d"%(i-16))
            else:
                self.__registradores[i].setNome('$s%d'%(i-16))
        # Reservados para tratamento de interrupções
        self.__registradores[26].setNome('$k0', True)
        self.__registradores[27].setNome('$k1', True)
        #
        self.__registradores[28].setNome('$gp')
        self.__registradores[28].setValor(hex(4295491585))
        self.__registradores[29].setNome('$sp', True)
        self.__registradores[30].setNome('$fp')
        self.__registradores[31].setNome('$ra')
        self.__registradores[32].setNome('$hi', True)
        self.__registradores[33].setNome('$lo', True)
    def getRegistrador (self, numero=None, nome=None):
        if numero:
            return self.buscaRegNum(numero)
        elif nome:
            return self.buscaRegNome(nome)
        else:
            raise Exception("Parâmetros inválidos")
    def buscaRegNome (self, nome):
        for registrador in self.__registradores:
            if registrador.getNome() == nome:
                return registrador
        return None
    def buscaRegNum (self, num):
        if 0 < num < len(self.__registradores):
            return self.__registradores[num]
        else:
            return None
    def load_word (self, regNome, var, regNum=None):
        try:
            if regNome:
                for registrador in self.__registradores:
                    if (registrador.getNome() == regNome):
                        registrador.setValor(var.getValor())
                        return True
                return False
            elif regNum:
                self.__registradores[regNum].setValor(var.getValor())
        except:
            raise Exception("Parâmetros inválidos")
    def getRegistradores (self):
        return self.__registradores