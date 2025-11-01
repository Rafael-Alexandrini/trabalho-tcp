from TocadorMidi import TocadorMidi
from SequenciaMidi import SequenciaMidi
import time

def meu_print():
    print("oi")

nova_seq_midi = SequenciaMidi()
lista_midi = [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]
nova_seq_midi.anexar_varias_mensagens_midi(lista_midi)
print(nova_seq_midi.get_lista_mensagens_midi())

meu_tocador = TocadorMidi()
meu_tocador.tocar(nova_seq_midi, comando_fim_musica=meu_print)

entrada = input("Digite algo: ")
while entrada:
    if entrada == '0':
        meu_tocador.parar()
    elif entrada == '1':
        meu_tocador.tocar(nova_seq_midi, meu_print)
    elif entrada == '2':
        meu_tocador.sair()
        break
    entrada = input("Digite algo: ")