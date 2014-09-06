# -*- encoding: UTF-8 -*-

from pyparsing import Literal, Regex, Word, OneOrMore, White
from pyparsing import Group, And, LineEnd, alphas, alphanums

def parse(string):
    # Tokens
    data = Word(".data")
    text = Literal(".text")
    globl = Literal(".globl")
    variavel = Regex(r'[a-zA-Z]*[a-zA-Z0-9]:')
    aspas = Literal('"').suppress()
    par_ab = Literal("(").suppress()
    par_fe = Literal(")").suppress()
    palavra = Word(alphanums)
    espacos = OneOrMore(White()).suppress()
    label = Word(alphas+":")
    virgula = Literal(",").suppress()
    instrucoes = r'(add[i|u|iu])|(add)|(subu)|(sub)|(mult)|(div)|'
    instrucoes += r'(li)|(lw)|(lhu)|(lh)|(lbu)|(lb)|(sw)|(sh)|(sb)|(lui)|(mfhi)|(mflo)|'
    instrucoes += r'(andi)|(and)|(ori)|(or)|(xor)|(nor)|(slti)|(slt)|'
    instrucoes += r'(beq)|(bne)|(jal)|(jr)|(j)'
    instrucao = Regex(instrucoes)
    registrador = Regex(r"(\$zero)|\$at|\$v0|\$v1|\$a4|\$[0-9]|\$[0-9][0-9]|\$a5|\$a6|\$a7|\$t0|\$t1|\$t2|\$t3|\$t4|\$t5|\$t6|\$t7|\$s0|\$s1|\$s2|\$s3|\$s4|\$s5|\$s6|\$s7|\$t8|\$t9|\$k0|\$k1|\$gp|\$sp|\$fp|\$ra|\$hi|\$lo")
    tipos = Regex(r'(\.word)|(\.asciiz)|(\.ascii)|(\.byte)|(\.half)|(\.float)|(\.double)|(\.space)|(\.align)')
    linha = LineEnd().suppress()
    # Grupos de Tokens
    inst_r = Group( registrador + virgula + (palavra | registrador) + virgula + (palavra | registrador) )
    inst_i = Group( (registrador) + virgula + ( ((palavra|registrador) + par_ab + (palavra|registrador) + par_fe) | (palavra|registrador) ) )
    inst_j = label
    # Grupos de grupos de tokens
    variaveis = Group( variavel + espacos + tipos + ( (aspas + palavra + aspas + linha) | (palavra + linha) | linha) )
    maisVariaveis = OneOrMore(variaveis)
    
    comandos = Group( instrucao + espacos + (inst_r | inst_i | inst_j) )
    maisComandos = OneOrMore(comandos)
    # Função sequencia
    programa = And([
        data,
        maisVariaveis | espacos,
        text,
        (globl + palavra + linha) | espacos,
        label,
        maisComandos
      ])
    # Lista de elementos
    return programa.parseString(string)