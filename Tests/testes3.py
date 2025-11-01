import pygame
import pygame.midi
import time

pygame.midi.init()
midi_output = pygame.midi.Output(pygame.midi.get_default_output_id(), latency=10)

# Obtém o timestamp atual para agendamento
agora = pygame.midi.time()

# Notas do acorde
do_central = 60
mi = 64
sol = 67
velocidade = 127
duracao = 1000

# Status bytes
NOTE_ON = 144  # Note On no canal 0
NOTE_OFF = 128 # Note Off no canal 0
PROGRAM_CHANGE = 192 # Mudar instrumento no canal 0

print("Tocando acorde com .write()...")

# Cria a lista de eventos MIDI
eventos = [
    # Mudar para o instrumento 0 (Piano) no momento 'agora'
    [[PROGRAM_CHANGE, 0, 0], agora],
]

for i in range(10):
    eventos.extend([
        # Iniciar todas as notas do acorde no momento 'agora'
        [[NOTE_ON, do_central, velocidade], agora + i * duracao + 200],
        [[NOTE_ON, mi, velocidade], agora + i * duracao + 200],
        [[NOTE_ON, sol, velocidade], agora + i * duracao + 200],

        # Parar todas as notas [duração] milissegundos depois
        [[NOTE_OFF, do_central, velocidade], agora + duracao + i * duracao],
        [[NOTE_OFF, mi, velocidade], agora + duracao + i * duracao],
        [[NOTE_OFF, sol, velocidade], agora + duracao + i * duracao]])
        


midi_output.write(eventos)

time.sleep(2)
midi_output.abort()
# Precisamos manter o programa rodando para dar tempo dos eventos agendados ocorrerem
time.sleep(5)
print("Eventos enviados.")

del midi_output
pygame.midi.quit()