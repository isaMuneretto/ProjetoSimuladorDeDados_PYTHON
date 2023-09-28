#Projeto 7- Jogo de aventura
#Um jogo de decisão onde eu terei que criar varios cenarios diferentes baseados nas respostas que forem dadas

# eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

#Qual é o cenário?: Eu estou em uma guerra entre duas nações e existe dois lados: LadoA e LadoB.
#Somente o ladoA irá vencer o ladoB irá perder. Entao eu tenho que tomas as decisoes corretas para
#chegar a vitoria, que somente o ladoA ira conseguir

import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s)' #norte = ladoA, sul = ladoB
        self.pergunta2 = 'Você prefere a espada ou o escudo? (espada/escudo)' #espada = ladoA, escudo = ladoB
        self.pergunta3 = 'Qual é sua especialidade? (linha de frente/tático)' #linha de frente = ladoA , tatico = ladoB
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegente todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'
    
    def Iniciar(self):
        #layout
        layout = [
            [sg.Output(size=(50,10))],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        #criar janela
        self.janela = sg.Window('Jogo de Aventura',layout=layout)
        while True:
            #ler os dados
            self.LerValores()
            #fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tático':
                        print(self.finalHistoria4)
            #verificacao para o evento win closed, não mostra a janela apos ser chamado
            if self.eventos == sg.WIN_CLOSED:
                break
    
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()