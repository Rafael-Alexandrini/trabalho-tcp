from SequenciaMidi import SequenciaMidi
from TocadorMidi import TocadorMidi
import pygame.midi
import time

nova_seq_midi = SequenciaMidi()
lista_midi = [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]
nova_seq_midi.anexar_varias_mensagens_midi(lista_midi)

toc = TocadorMidi()
toc.tocar(nova_seq_midi)
toc.parar()
toc.tocar(nova_seq_midi)

time.sleep(10)