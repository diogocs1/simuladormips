# -*- encoding: UTF-8 -*-

import thread, gtk
import webbrowser

from bottle import route, run, template, static_file, request, redirect
import controller
from lib.simulador import Sistema


# Mantém o dicionário de contexto globalmente
sys = None
contexto = {}

@route("/")
def inicio ():
    '''
    Carrega a página inicial
    '''
    global contexto, sys
    sys = Sistema()
    contexto = {
                "registradores":sys.getBanco().getRegistradores(),
                "variaveis":None,
                'instrucoes': None,
                'UC': None,
                'ULA' : None,
                "codigo":"Digite o código no campo ao lado",
                "erro":None,
                'simulando': False,
                'proxima_instrucao': None,
                'decimal': False,
                'sys':sys
                }
    return template("template/index.html", contexto)

@route("/", method="POST")
def simular ():
    '''
    Executa o método POST para receber o código digitado
    '''
    global contexto
    
    if request.POST.get("simular",''):
        cod = request.POST.get("cod",'').strip()
        # Inicializa e configura a Máquina
        contexto['sys'] = controller.inicializa(cod, sys)
        contexto['variaveis'] = contexto['sys'].getMemoriaDados().getDados()
        contexto['codigo'] = cod
        contexto['simulando'] = True
        contexto['ULA'] = contexto['sys'].getULA()
        contexto['proxima_instrucao'] = contexto['sys'].getProximaInstrucao()
        return template("template/index.html", contexto)
    elif request.POST.get('passo',''):
        # Executa uma única instrunção da fila
        contexto['sys'] = controller.executa(contexto["sys"])
        contexto['UC'] = contexto['sys'].getUC()
        contexto['ULA'] = contexto['sys'].getULA()
        contexto['proxima_instrucao'] = contexto['sys'].getProximaInstrucao()
        return template('template/index.html', contexto)
    
@route("/<tipo>")
def trocar_notacao(tipo):
    global contexto
    if tipo == "decimal":
        contexto['decimal'] = True
    else:
        contexto['decimal'] = False
    redirect("/")
    
@route("/reinicia/")
def reinicia ():
    redirect("/")

@route('/static/:path#.+#', name='static')
def static(path):
    '''
    Disponibiliza o diretório template para o navegador
    '''
    return static_file(path, root='template')


# iniciando o programa
if __name__ == '__main__':
    try:
        thread.start_new_thread(run, ())
        thread.start_new_thread(webbrowser.open_new_tab, ("http://localhost:8080",))
    except:
        print "Ocorreu um erro ao iniciar a aplicação"
        try:
            message = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK)
            message.set_markup("Ocorreu um erro ao iniciar a aplicação")
            message.run()
        except:
            pass
    while 1:
        pass
