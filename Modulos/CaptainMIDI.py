from Janela import Janela

TITLE = "Captain MIDI"
MAIN_WINDOW_PADDING = (3, 3, 12, 12)

OITAVAS = ('1', '2', '3', '4', '5', '6', '7', '8')
INSTRUMENTOS = ('#1 Piano', '#45 Guitar', '#12 Violin', '#112 Drums')
SCALE_LENGTH = 130

TEXTO_INICIAL = "Escreva o texto aqui..."

TABELA_CARACTERES_ESQ = "A / a\nB / b\nC / c\nD / d\nE / e\nF / f\nG / g\nH / h\n'Espaço'"
TABELA_FUNCAO_ESQ = "Lá\nSi\nDó\nRé\nMi\nFá\nSol\nSi bemol\nDobra Volume Atual"
TABELA_CARACTERES_DIR = "OIT+\nOIT-\nOutras vogais\n?\n'Nova linha'\nBPM+\n;"
TABELA_FUNCAO_DIR = "Aumenta uma oitava\nDiminui uma oitava\nRepete última nota\nNota aleatória\nTroca Instrumento\nAumenta BPM em 80\nPausa / Silêncio"

def get_instrument_number(instrument: str) -> int:
    number = instrument.split(' ')[0]
    return int(number[1:])

janela_principal = Janela(TITLE, MAIN_WINDOW_PADDING)

janela_principal.add_menu_command('Save txt', lambda: print('Save txt file'))
janela_principal.add_menu_command('Save MIDI', lambda: print('Save MIDI file'))
janela_principal.add_menu_command('Load txt', lambda: print('Load txt file'))

janela_principal.create_text_label("Captain MIDI", 0, 0, 'n', "Arial 20 bold", 4)

janela_principal.create_text_label("Oitava:", 0, 1, 'sw')
caixa_oitava = janela_principal.create_combobox(OITAVAS, janela_principal.get_octave_var(), 0, 2, 'nwe')

janela_principal.create_text_label("Instrumento:", 1, 1, 'sw')
caixa_instrumento = janela_principal.create_combobox(INSTRUMENTOS, janela_principal.get_instrument_var(), 1, 2, 'nwe')

escala_volume = janela_principal.create_horizontal_scale_with_label("Volume :", 0, 100, 20, janela_principal.get_vol_var(), 
                                                    SCALE_LENGTH, 2, 2, 'nwe')

escala_bpm = janela_principal.create_horizontal_scale_with_label("BPM :", 0, 300, 120, janela_principal.get_bpm_var(), 
                                                    SCALE_LENGTH, 3, 2, 'nwe')

texto = janela_principal.create_text_widget(50, 10, TEXTO_INICIAL, 0, 3, "nwes", 4)

botao_play = janela_principal.create_button("Play", lambda: print("Play button pressed"), 3, 4, "we")

janela_principal.create_text_label(TABELA_CARACTERES_ESQ, 0, 5, 'ne')
janela_principal.create_text_label(TABELA_FUNCAO_ESQ, 1, 5, 'nw')
janela_principal.create_text_label(TABELA_CARACTERES_DIR, 2, 5, 'ne')
janela_principal.create_text_label(TABELA_FUNCAO_DIR, 3, 5, 'nw')

janela_principal.bind_combobox_event(caixa_instrumento, 
    lambda e: print(f"Selected instrument: {get_instrument_number(janela_principal.get_instrument())}"))

janela_principal.set_paddings(5, 5)
janela_principal.set_weights(4, 6)

janela_principal.start_mainloop()