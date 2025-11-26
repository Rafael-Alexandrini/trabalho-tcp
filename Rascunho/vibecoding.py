import time
import pygame.midi


def interface(midi_output):
    entrada = input("Digite seu input ou digite 0 para terminar: ")
    while entrada != '0':
        decoder(entrada=entrada, midi_output=midi_output)
        
        
        
        
        
        entrada = input("Digite seu input ou digite 0 para terminar: ")

def decoder(entrada: str, midi_output):
    BPM = 160
    PAUSA_MS = 1000 * 60 / BPM # intervalo (ms) = 1000 * 1/BPS = 1000 * 1/(BPM/60)
    NOTE_ON = 144  # Note On no canal 0
    NOTE_OFF = 128 # Note Off no canal 0
    PROGRAM_CHANGE = 192 # Mudar instrumento no canal 0
    agora = pygame.midi.time()
    oitava_atual = 60
    velocidade = 100
    eventos = [
    # Mudar para o instrumento 1 no momento 'agora'
        [[PROGRAM_CHANGE, 1, 0], agora]
    ]
    timestamp = agora
    for char in entrada:
        match char:
            case 'A':
                eventos.append([[NOTE_ON, oitava_atual + 9, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 9, velocidade], timestamp])
            case 'H':
                eventos.append([[NOTE_ON, oitava_atual + 10, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 10, velocidade], timestamp])
            case 'B':
                eventos.append([[NOTE_ON, oitava_atual + 11, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 11, velocidade], timestamp])
            case 'C':
                eventos.append([[NOTE_ON, oitava_atual - 0, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual - 0, velocidade], timestamp])
            case 'D':
                eventos.append([[NOTE_ON, oitava_atual + 2, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 2, velocidade], timestamp])
            case 'E':
                eventos.append([[NOTE_ON, oitava_atual + 4, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 4, velocidade], timestamp])
            case 'F':
                eventos.append([[NOTE_ON, oitava_atual + 5, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 5, velocidade], timestamp])
            case 'G':
                eventos.append([[NOTE_ON, oitava_atual + 7, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual + 7, velocidade], timestamp])
            case '?' | '.':
                oitava_atual += 12
            case '-':
                oitava_atual -= 12
            case 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h':
                timestamp += PAUSA_MS
    
    midi_output.write(eventos)
    


if __name__ == "__main__":
    pygame.midi.init()
    midi_output = pygame.midi.Output(pygame.midi.get_default_output_id(), latency=10)
    interface(midi_output)
    del midi_output
    pygame.midi.quit()

# exemplo:
# tema do tetris
# EEBCDDCBAAACEEDCBBBCDDEECCAAAAaaaDDF.AA-GFEEECEEDCBBBCDDEECCAAAA
# '-' não existe na especificação do professor, mas shhh, eu quero diminuir a oitava mais facilmente

# -FA.FGAGFC-H.DA.C-AF-aaaFA.FGAGFC-H.DA.C-AFaaa
# :)
# OIT-FAOIT+FGAGFCOIT-HOIT+DAOIT+COIT-AFOIT-\n;;;FAOIT+FGAGFCOIT-HOIT+DAOIT+COIT-AFOIT+;;;