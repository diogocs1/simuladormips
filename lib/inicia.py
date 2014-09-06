# -*- encoding: UTF-8 -*-
from lib.memoria import Variavel
from lib.pyparsing import ParseResults
import re
from lib.instrucoes import Instrucao_R_I, Instrucao_J

def configura (parse_result, sys):
    '''
    Formato do ParseResult:
    ['.data', ['var1', '.asciiz'], ['var2', '.asciiz', 'diogo'], ['var3', '.asciiz', 'diogo'], ['var4', '.asciiz', 'diogo'], '.text', '.globl', 'main', 'main:', ['addi', ['$t1', '$zero', '6']]]
    '''
    # Identifica as variáveis
    for item in parse_result:
        if item == '.data':
            continue
        # Pegando variáveis com e sem o valor declarado
        elif type(item) is ParseResults:
            try:
                var = Variavel(item[0], item[1], item[2])
            except:
                try:
                    var = Variavel(item[0], item[1])
                except:
                    raise Exception("Variável inválida: %s  %s  %s" %(item[0], item[1]))
            sys.getMemoriaDados().setDado(var)
        elif item == '.text':
            break
    # identificando os comandos
    for i in range(len(parse_result)):
        comando = None
        if parse_result[i] == ".text":
            # identificando os coamndos depois do bloco ".text"
            for j in range(i, len(parse_result)):
                if type(parse_result[j]) is str:
                    if re.match(r'[a-zA-Z]*[:]', parse_result[j]):
                        comando = parse_result[j]
                        sys.getMemoriaInstrucao().setDado(comando)
                elif type(parse_result[j]) is ParseResults:
                    try:
                        comando = Instrucao_R_I(parse_result[j][0], parse_result[j][1][0], parse_result[j][1][1], parse_result[j][1][2] )
                        sys.getMemoriaInstrucao().setDado(comando)
                    except:
                        try:
                            comando = Instrucao_R_I(parse_result[j][0], parse_result[j][1][0], parse_result[j][1][1])
                            sys.getMemoriaInstrucao().setDado(comando)
                        except:
                            try:
                                comando = Instrucao_J(parse_result[j][0], parse_result[j][1][0])
                                sys.getMemoriaInstrucao().setDado(comando)
                            except:
                                raise Exception("Instrunção não identificada 2: %s" % (parse_result[j]))
            break
    print sys.getMemoriaInstrucao().getDados()
    return sys