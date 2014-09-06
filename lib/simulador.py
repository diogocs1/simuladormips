# -*- encoding: UTF-8 -*-

from controle import UC
from lib.memoria import Mem_instrucoes, Mem_dados
from lib.registradores import Banco
from lib.operacoes import ULA
from lib.instrucoes import Instrucao_R_I

class Sistema (object):
    def __init__(self):
        self.__PC = 0
        self.__UC = UC()
        self.__ULA = ULA()
        self.__memoriaInstrucao = Mem_instrucoes()
        self.__memoriaDados = Mem_dados()
        self.__bancoDeRegistradores = Banco()

    def executaInstrucao (self):
        instrucao = self.__memoriaInstrucao.getInstrucao(self.__PC)
        valores = self.decodifica(instrucao)
        if valores:
            self.__ULA.opera(self.__UC, instrucao, valores)
        self.incrementaPC()
    def decodifica (self, instrucao):
        '''
        Função: decodifica(instrucao)
        Descrição: Localiza e retorna valores de registradores e variáveis 
        '''
        # Verifica se o PC aponta para um Label
        if type(instrucao) is str:
            return None
        self.__UC.decodifica(instrucao)
        if type(instrucao) is Instrucao_R_I:
            resultado = instrucao.getResultado()
            valor2 = None
            # buscando o primeiro registrador
            resultado = self.__bancoDeRegistradores.getRegistrador(nome=resultado)
            # buscando operando 1
            valor1 = instrucao.getValor1()
            print valor1
            if self.__bancoDeRegistradores.getRegistrador(nome=valor1):
                valor1 = self.__bancoDeRegistradores.getRegistrador(nome=valor1).getValor()
            elif self.__memoriaDados.getDado(nome=valor1):
                valor1 = self.__memoriaDados.getDado(valor1).getValor()
            # buscando operando 2
            if instrucao.getValor2():
                valor2 = instrucao.getValor2()
                if self.__bancoDeRegistradores.getRegistrador(nome=valor2):
                    valor2 = self.__bancoDeRegistradores.getRegistrador(nome=valor2).getValor()
                elif self.__memoriaDados.getDado(nome=valor2):
                    valor2 = self.__memoriaDados.getDado(valor2).getValor()
            return [resultado, valor1, valor2]
                
        else:
            endereco = instrucao.getEndereco()
            fila_de_inst = self.__memoriaInstrucao.getDados()
            for inst in fila_de_inst:
                if inst == endereco:
                    self.__PC = fila_de_inst.index(inst)
            return None
        return None
    def getPC(self):
        return self.__PC
    def getProximaInstrucao(self):
        try:
            return self.__memoriaInstrucao.getInstrucao(self.__PC)
        except:
            return "Fim do programa!"
    def setPC (self, indice):
        self.__PC = indice
    def incrementaPC(self):
        self.__PC += 1
    def getIR (self):
        return self.__IR
    def getMDR (self):
        return self.__MDR
    def getA (self):
        return self.__A
    def getB (self):
        return self.__B
    def getULA (self):
        return self.__ULA
    def getUC(self):
        return self.__UC
    def getMemoriaInstrucao(self):
        return self.__memoriaInstrucao
    def getMemoriaDados(self):
        return self.__memoriaDados
    def getBanco (self):
        return self.__bancoDeRegistradores
        