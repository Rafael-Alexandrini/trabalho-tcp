from Janela import Janela
from TocadorMidi import TocadorMidi
from DecodificadorMidi import DecodificadorMidi
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk

class CaptainMIDI:
    def __init__(self):
        INSTRUMENTO_INICIAL = 0
        BPM_INICIAL = 120
        OITAVA_INICIAL = 4
        VOLUME_INICIAL = 60
        self.tocador = TocadorMidi()
        self.decodificador = DecodificadorMidi(BPM_INICIAL, INSTRUMENTO_INICIAL, OITAVA_INICIAL, VOLUME_INICIAL)

        TITLE = "Captain MIDI"
        MAIN_WINDOW_PADDING = (3, 3, 12, 12)

        OITAVAS = ('0', '1', '2', '3', '4', '5', '6', '7', '8')
        INSTRUMENTOS = ('#000 Acoustic Grand Piano', '#009 Glockenspiel', '#016 Drawbar Organ', '#024 Acoustic Guitar', '#032 Acoustic Bass', '#040 Violin', '#073 Flute', '#088 Pad 1','#114 Steel Drums', '#124 Telephone Ring')
        SCALE_LENGTH = 130

        TEXTO_INICIAL = "Escreva o texto aqui..."

        TABELA_CARACTERES_ESQ = "A / a\nB / b\nC / c\nD / d\nE / e\nF / f\nG / g\nH / h\n'Espaço'"
        TABELA_FUNCAO_ESQ = "Lá\nSi\nDó\nRé\nMi\nFá\nSol\nSi bemol\nDobra Volume Atual"
        TABELA_CARACTERES_DIR = "OIT+\nOIT-\nOutras vogais\n?\n'Nova linha'+ 3 Dígitos\nBPM+\nBPM-\n;"
        TABELA_FUNCAO_DIR = "Aumenta uma oitava\nDiminui uma oitava\nRepete última nota\nNota aleatória\nTroca Instrumento\nAumenta BPM em 20\nDiminui BPM em 20\nPausa / Silêncio"


        self.janela_principal = Janela(TITLE, MAIN_WINDOW_PADDING)

        self.janela_principal.add_menu_command('Save txt', self.salvar_texto)
        self.janela_principal.add_menu_command('Save MIDI', self.salva_sequencia)
        self.janela_principal.add_menu_command('Load txt', self.carregar_texto)

        self.janela_principal.create_text_label("Captain MIDI", 0, 0, 'n', "Arial 20 bold", 4)

        self.janela_principal.create_text_label("Oitava:", 0, 1, 'sw')
        oitava = self.janela_principal.init_string_var()
        self.caixa_oitava = self.janela_principal.create_combobox(OITAVAS, oitava, 0, 2, 'nwe', initial_index=OITAVA_INICIAL)

        self.janela_principal.create_text_label("Instrumento:", 1, 1, 'sw')
        self.instrumento = self.janela_principal.init_string_var()
        caixa_instrumento = self.janela_principal.create_combobox(INSTRUMENTOS, self.instrumento, 1, 2, 'nwe')

        self.volume = self.janela_principal.init_int_var()
        escala_volume = self.janela_principal.create_horizontal_scale_with_label("Volume :", 0, 127, 100, self.volume, 
                                                                            SCALE_LENGTH, 2, 2, 'nwe')

        self.bpm = self.janela_principal.init_int_var()
        escala_bpm = self.janela_principal.create_horizontal_scale_with_label("BPM :", 40, 240, 120, self.bpm, 
                                                                        SCALE_LENGTH, 3, 2, 'nwe')

        self.texto = self.janela_principal.create_text_widget(50, 10, TEXTO_INICIAL, 0, 3, "nwes", 4)

        self.botao_play = self.janela_principal.create_button("Play", self.play, 3, 4, "we")

        self.janela_principal.create_text_label(TABELA_CARACTERES_ESQ, 0, 5, 'ne')
        self.janela_principal.create_text_label(TABELA_FUNCAO_ESQ, 1, 5, 'nw')
        self.janela_principal.create_text_label(TABELA_CARACTERES_DIR, 2, 5, 'ne')
        self.janela_principal.create_text_label(TABELA_FUNCAO_DIR, 3, 5, 'nw')

        self.janela_principal.set_paddings(5, 5)
        self.janela_principal.set_weights(4, 6)

        
        

    def play(self):
        self.tocador.parar()
        self.decodificador.set_bpm_padrao(self.janela_principal.get_intvar_value(self.bpm))
        self.decodificador.set_instrumento_padrao(self.get_instrument_number(self.janela_principal.get_strvar_string(self.instrumento)))
        self.decodificador.set_oitava_padrao(self.janela_principal.get_combobox_current_index(self.caixa_oitava))
        self.decodificador.set_volume_padrao(self.janela_principal.get_intvar_value(self.volume))
        text = self.janela_principal.get_text(self.texto)
        sequencia = self.decodificador.texto_para_sequencia_midi(text)
        self.tocador.tocar(sequencia, self.stop)
        self.janela_principal.set_button_text(self.botao_play, "Parar")
        self.janela_principal.set_button_commmand(self.botao_play, self.stop)    

    def stop(self):
        self.tocador.parar()
        self.janela_principal.set_button_text(self.botao_play, "Tocar")
        self.janela_principal.set_button_commmand(self.botao_play, self.play)  

    def salvar_texto(self):
            Tk().withdraw()

            save_path = asksaveasfilename(
                title="Save text file as ...",
                defaultextension=".txt",
                filetypes=[("text files", "*.txt")],
                initialdir="../Salvos/"
            )

            if save_path:
                with open(save_path,"w") as f:
                    f.write(self.janela_principal.get_text(self.texto))

    def carregar_texto(self):
        Tk().withdraw()

        load_path = askopenfilename(
            title="Select a text file ...",
            defaultextension=".txt",
            filetypes=[("text files", "*.txt")],
            initialdir="../Salvos/"
        )

        if load_path:
            with open(load_path,"r") as f:
                self.janela_principal.set_text(self.texto, f.read())

    def salva_sequencia(self):
        self.tocador.parar()
        self.decodificador.set_bpm_padrao(self.janela_principal.get_intvar_value(self.bpm))
        self.decodificador.set_instrumento_padrao(self.get_instrument_number(self.janela_principal.get_strvar_string(self.instrumento)))
        self.decodificador.set_oitava_padrao(self.janela_principal.get_combobox_current_index(self.caixa_oitava))
        self.decodificador.set_volume_padrao(self.janela_principal.get_intvar_value(self.volume))
        text = self.janela_principal.get_text(self.texto)
        sequencia = self.decodificador.texto_para_sequencia_midi(text)
        Tk().withdraw()
        save_path = asksaveasfilename(
            title="Save MIDI file as...",
            defaultextension=".mid",
            filetypes=[("MIDI files", "*.mid *.midi")],
            initialdir="../Salvos"
        )
        sequencia.salva_midi(save_path)

    def get_instrument_number(self, instrument: str) -> int:
        number = instrument.split(' ')[0]
        return int(number[1:])

    def start_mainloop(self):
        self.janela_principal.start_mainloop()
        self.tocador.parar()

captainMidi = CaptainMIDI()
captainMidi.start_mainloop()