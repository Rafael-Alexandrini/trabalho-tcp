import pygame.midi
import time

pygame.midi.init()
player = pygame.midi.Output(0)
"""player.set_instrument(65, 0)
player.note_on(64, 127)
time.sleep(0.5)
player.set_instrument(20, 1)
player.note_on(64, 127, 1)
time.sleep(0.5)
player.note_off(64, 0, 0)
time.sleep(1)
player.note_off(64, 0, 1)
time.sleep(1)"""

player.write([[[0xc0, 0, 0], 20000], [[0x90, 60, 100], 20500], [[0x90, 64, 100], 20500], [[0x80, 60, 100], 42500], [[0x80, 64, 100], 42500]])
time.sleep(10)
del player
pygame.midi.quit()

