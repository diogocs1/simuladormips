# -*- encoding: UTF-8 -*-

from lib.parser import parse
from lib.inicia import configura

def inicializa (cod,sys):
    resultado = parse(cod)
    print resultado
    sys = configura(resultado, sys)
    return sys

def executa (sys):
    sys.executaInstrucao()
    return sys