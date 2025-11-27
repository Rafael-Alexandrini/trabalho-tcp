from Janela import Janela
from TocadorMidi import TocadorMidi
from DecodificadorMidi import DecodificadorMidi
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk

def play():
    global janela_principal, tocador, decodificador, caixa_oitava, texto
    tocador.parar()
    decodificador.set_bpm_padrao(janela_principal.get_intvar_value(bpm))
    decodificador.set_instrumento_padrao(get_instrument_number(janela_principal.get_strvar_string(instrumento)))
    decodificador.set_oitava_padrao(janela_principal.get_combobox_current_index(caixa_oitava))
    decodificador.set_volume_padrao(janela_principal.get_intvar_value(volume))
    text = janela_principal.get_text(texto)
    sequencia = decodificador.texto_para_sequencia_midi(text)
    tocador.tocar(sequencia, stop)
    janela_principal.set_button_text(botao_play, "Parar")
    janela_principal.set_button_commmand(botao_play, stop)    

def stop():
    global tocador, janela_principal, botao_play
    tocador.parar()
    janela_principal.set_button_text(botao_play, "Tocar")
    janela_principal.set_button_commmand(botao_play, play)  

def salvar_texto():
        global janela_principal
        Tk().withdraw()

        save_path = asksaveasfilename(
            title="Save text file as ...",
            defaultextension=".txt",
            filetypes=[("text files", "*.txt")],
            initialdir="../Salvos/"
        )

        if save_path:
            with open(save_path,"w") as f:
                f.write(janela_principal.get_text(texto))

def carregar_texto():
    Tk().withdraw()

    load_path = askopenfilename(
        title="Select a text file ...",
        defaultextension=".txt",
        filetypes=[("text files", "*.txt")],
        initialdir="../Salvos/"
    )

    if load_path:
        with open(load_path,"r") as f:
            janela_principal.set_text(texto, f.read())

INSTRUMENTO_INICIAL = 0
BPM_INICIAL = 120
OITAVA_INICIAL = 4
VOLUME_INICIAL = 60
tocador = TocadorMidi()
decodificador = DecodificadorMidi(BPM_INICIAL, INSTRUMENTO_INICIAL, OITAVA_INICIAL, VOLUME_INICIAL)

TITLE = "Captain MIDI"
MAIN_WINDOW_PADDING = (3, 3, 12, 12)

OITAVAS = ('0', '1', '2', '3', '4', '5', '6', '7', '8')
INSTRUMENTOS = ('#000 Acoustic Grand Piano', '#009 Glockenspiel', '#024 Acoustic Guitar', '#40 Violin', '#40 Violin', '#114 Steel Drums', '#124 Telephone Ring')
SCALE_LENGTH = 130

TEXTO_INICIAL = "Escreva o texto aqui..."

TABELA_CARACTERES_ESQ = "A / a\nB / b\nC / c\nD / d\nE / e\nF / f\nG / g\nH / h\n'Espaço'"
TABELA_FUNCAO_ESQ = "Lá\nSi\nDó\nRé\nMi\nFá\nSol\nSi bemol\nDobra Volume Atual"
TABELA_CARACTERES_DIR = "OIT+\nOIT-\nOutras vogais\n?\n'Nova linha'+ 3 Dígitos\nBPM+\nBPM-\n;"
TABELA_FUNCAO_DIR = "Aumenta uma oitava\nDiminui uma oitava\nRepete última nota\nNota aleatória\nTroca Instrumento\nAumenta BPM em 20\nDiminui BPM em 20\nPausa / Silêncio"

def get_instrument_number(instrument: str) -> int:
    number = instrument.split(' ')[0]
    return int(number[1:])

janela_principal = Janela(TITLE, MAIN_WINDOW_PADDING)

janela_principal.add_menu_command('Save txt', salvar_texto)
janela_principal.add_menu_command('Save MIDI', lambda: print('Save MIDI file'))
janela_principal.add_menu_command('Load txt', carregar_texto)

janela_principal.create_text_label("Captain MIDI", 0, 0, 'n', "Arial 20 bold", 4)

janela_principal.create_text_label("Oitava:", 0, 1, 'sw')
oitava = janela_principal.init_int_var()
caixa_oitava = janela_principal.create_combobox(OITAVAS, oitava, 0, 2, 'nwe')

janela_principal.create_text_label("Instrumento:", 1, 1, 'sw')
instrumento = janela_principal.init_string_var()
caixa_instrumento = janela_principal.create_combobox(INSTRUMENTOS, instrumento, 1, 2, 'nwe')

volume = janela_principal.init_int_var()
escala_volume = janela_principal.create_horizontal_scale_with_label("Volume :", 0, 127, 20, volume, 
                                                                    SCALE_LENGTH, 2, 2, 'nwe')

bpm = janela_principal.init_int_var()
escala_bpm = janela_principal.create_horizontal_scale_with_label("BPM :", 40, 240, 120, bpm, 
                                                                 SCALE_LENGTH, 3, 2, 'nwe')

texto = janela_principal.create_text_widget(50, 10, TEXTO_INICIAL, 0, 3, "nwes", 4)

botao_play = janela_principal.create_button("Play", play, 3, 4, "we")

janela_principal.create_text_label(TABELA_CARACTERES_ESQ, 0, 5, 'ne')
janela_principal.create_text_label(TABELA_FUNCAO_ESQ, 1, 5, 'nw')
janela_principal.create_text_label(TABELA_CARACTERES_DIR, 2, 5, 'ne')
janela_principal.create_text_label(TABELA_FUNCAO_DIR, 3, 5, 'nw')

janela_principal.set_paddings(5, 5)
janela_principal.set_weights(4, 6)

janela_principal.start_mainloop()
tocador.parar()