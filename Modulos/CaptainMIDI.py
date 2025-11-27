from Janela import Janela

TITLE = "Captain MIDI"
MAIN_WINDOW_PADDING = (3, 3, 12, 12)

OITAVAS = ('1', '2', '3', '4', '5', '6', '7', '8')
INSTRUMENTOS = ('Piano', 'Guitar', 'Violin', 'Drums')
SCALE_LENGTH = 130

TEXTO_INICIAL = "Escreva o texto aqui..."

DICIONARIO_CARACTERES = "C D E F G A B c d e f g a b"

janela_principal = Janela(TITLE, MAIN_WINDOW_PADDING)

janela_principal.add_menu_command('Save txt', lambda: print('Save txt file'))
janela_principal.add_menu_command('Save MIDI', lambda: print('Save MIDI file'))
janela_principal.add_menu_command('Load txt', lambda: print('Load txt file'))

janela_principal.create_text_label("Captain MIDI", 0, 0, 'n', "Arial 20 bold", colspan=4)

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

janela_principal.create_text_label(DICIONARIO_CARACTERES, 0, 5, '', colspan=4)

janela_principal.set_paddings(5, 5)
janela_principal.set_weights(4, 6)

janela_principal.start_mainloop()