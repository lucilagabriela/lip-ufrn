from random import shuffle
from threading import Thread
from gtts import gTTS
from playsound import playsound
from os import remove
from time import sleep

class Bingo:

    def __init__(self, qtd_numeros=90):
        self.pausado = False
        self.finalizado = False
        self.numeros = list(range(1, qtd_numeros+1))
        shuffle(self.numeros)
        self.sorteados = []
        self.observador_externo = None

    def adicionar_observador(self, observador):
        self.observador_externo = observador

    def mostrar_parcial(self):
        print("Números sorteados: ")
        print(sorted(self.sorteados))

    def restam_numeros(self):
        return len(self.numeros) > 0

    def sortear_numero(self):
        if self.restam_numeros():
            ultimo = self.numeros.pop()
            self.sorteados.append(ultimo)
            return ultimo
        else:
            return None


    def ultimo_sorteado(self):
        if len(self.sorteados) > 0:
            return self.sorteados[-1]
        else:
            return 'N/D'

    def finalizar(self):
        self.finalizado = True

    def play_pause(self):
        if self.pausado is True:
            self.pausado = False
        else:
            self.pausado = True


    def mostrar_detalhes(self):
        print(self.numeros)

    def realizar_contagem(self):
        for i in range(5,0,-1):
            Locutor.falar_frase(i)
            if self.observador_externo is not None:
                self.observador_externo.set(str(i))
            playsound('beep.mp3')
    

    def executar(self):
        Locutor.falar_frase("Cartela na mão, o jogo vai começar.")
        self.realizar_contagem()
        while self.restam_numeros() and self.finalizado is not True:
            numero = self.sortear_numero()
            if self.observador_externo is not None:
                self.observador_externo.set(str(numero))
            Locutor.cantar_numero(numero)
            self.mostrar_parcial()
            sleep(4)
            if self.pausado is True:
                playsound('sirene.mp3')
                Locutor.falar_frase("Alguém disse")
                playsound('bingo.mp3')
                Locutor.falar_frase("Vamos conferir")
                while self.pausado is True and self.finalizado is not True:
                    sleep(1)
        Locutor.falar_frase("Parabéns ao vencedor.")
        playsound('palmas.wav')

    def run(self):
        t = Thread(target=self.executar)
        t.start()    



class Locutor:

    frases = {
        1: "Se liga, começou o jogo.",
        22: "Dois patinhos na lagoa",
        71: "A bruxa",
        51: "Uma boa ideia",
        90: "Fim do jogo",
    }

    def falar_frase(frase):
        if type(frase) is not str:
            frase = str(frase)
        audio = gTTS(frase, lang='pt', slow=False)
        audio.save('audio.mp3')
        playsound('audio.mp3')
        remove('audio.mp3')

    def fazer_graca(numero):
        if numero in Locutor.frases.keys():
            Locutor.falar_frase(Locutor.frases[numero])

    def cantar_numero(numero):
        Locutor.falar_frase(numero)
        Locutor.fazer_graca(numero)


