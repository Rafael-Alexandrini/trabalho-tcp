import tkinter as tk
from tkinter import messagebox
import pygame.midi

def criar_gradiente(canvas, cor1, cor2):
    """Cria um gradiente de cor vertical no canvas."""
    largura = int(canvas.cget("width"))
    altura = int(canvas.cget("height"))
    
    # Itera sobre cada linha do canvas para desenhar o gradiente
    for i in range(altura):
        # Interpolação linear das cores
        r1, g1, b1 = canvas.winfo_rgb(cor1)
        r2, g2, b2 = canvas.winfo_rgb(cor2)
        
        # Calcula a cor intermediária para a linha atual
        novo_r = int(r1 + (r2 - r1) * (i / altura))
        novo_g = int(g1 + (g2 - g1) * (i / altura))
        novo_b = int(b1 + (b2 - b1) * (i / altura))
        
        # Formata a cor no formato hexadecimal que o Tkinter entende
        cor = f'#{novo_r:04x}{novo_g:04x}{novo_b:04x}'
        
        # Desenha uma linha com a cor calculada
        canvas.create_line(0, i, largura, i, fill=cor)

def acao_botao_ok():
    """Função chamada quando o botão 'OK' é pressionado."""    

    texto_digitado = campo_input.get()
    if texto_digitado:
        decoder(texto_digitado)
    else:
        messagebox.showwarning("Atenção", "Por favor, digite algo no campo de texto.")

def acao_botao_sair():
    """Função chamada quando o botão 'Sair' é pressionado."""
    janela.quit()

def decoder(entrada: str):
    global midi_output
    BPM = 160
    PAUSA_MS = 1000 * 60 / BPM # intervalo (ms) = 1000 * 1/BPS = 1000 * 1/(BPM/60)
    NOTE_ON = 144  # Note On no canal 0
    NOTE_OFF = 128 # Note Off no canal 0
    PROGRAM_CHANGE = 192 # Mudar instrumento no canal 0
    agora = pygame.midi.time()
    oitava_atual = 60
    velocidade = 100
    eventos = [
    # Mudar para o instrumento 20 no momento 'agora'
        [[PROGRAM_CHANGE, 109, 0], agora]
    ]
    timestamp = agora
    for char in entrada:
        match char:
            case 'A':
                eventos.append([[NOTE_ON, oitava_atual - 3, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual - 3, velocidade], timestamp])
            case 'H':
                eventos.append([[NOTE_ON, oitava_atual - 2, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual - 2, velocidade], timestamp])
            case 'B':
                eventos.append([[NOTE_ON, oitava_atual - 1, velocidade], timestamp])
                timestamp += PAUSA_MS
                eventos.append([[NOTE_OFF, oitava_atual - 1, velocidade], timestamp])
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

# --- Configuração da Janela Principal ---
janela = tk.Tk()
janela.title("Captain MIDI feat. Lil' LM")
janela.geometry("400x300")
janela.resizable(False, False)

# --- Fundo com Gradiente ---
# Cria um Canvas que ocupará toda a janela
canvas_gradiente = tk.Canvas(janela, width=400, height=300)
canvas_gradiente.pack(fill="both", expand=True)

# Define as cores do gradiente e o cria
cor_inicial = "#ADD8E6"  # Azul claro
cor_final = "#4682B4"     # Azul aço
criar_gradiente(canvas_gradiente, cor_inicial, cor_final)

# --- Widgets da Interface ---

# Rótulo de Texto (Label)
# O Canvas é usado como 'master' para que o widget apareça sobre o gradiente
label_texto = tk.Label(canvas_gradiente, text="EEBCDDCBAAACEEDCBBBCDDEECCAAAA", font=("Arial", 14), bg=cor_final, fg="white")
canvas_gradiente.create_window(200, 50, window=label_texto)

# Campo de Input de Texto (Entry)
campo_input = tk.Entry(canvas_gradiente, font=("Arial", 12), width=30)
canvas_gradiente.create_window(200, 100, window=campo_input)

# Botão "OK"
botao_ok = tk.Button(canvas_gradiente, text="OK", font=("Arial", 12, "bold"), command=acao_botao_ok, relief=tk.RAISED, borderwidth=3)
canvas_gradiente.create_window(150, 160, window=botao_ok)

# Botão "Sair"
botao_sair = tk.Button(canvas_gradiente, text="Sair", font=("Arial", 12, "bold"), command=acao_botao_sair, relief=tk.RAISED, borderwidth=3)
canvas_gradiente.create_window(250, 160, window=botao_sair)

# Inicia o loop principal da aplicação para que a janela seja exibida

pygame.midi.init()
midi_output = pygame.midi.Output(pygame.midi.get_default_output_id(), latency=10)
janela.mainloop()
del midi_output
pygame.midi.quit()


