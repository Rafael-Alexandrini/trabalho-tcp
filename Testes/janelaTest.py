from Janela import Janela

janelaPrincipal = Janela("Captain MIDI", (10, 10, 10, 10))
janelaPrincipal.create_text_widget(50, 10, "C D E F G A B", 2, 1, "we")
janelaPrincipal.create_button("Play", lambda: print("Play button pressed"), 3, 3, "we")
janelaPrincipal.create_text_label("Text:", 1, 1, "ne")
janelaPrincipal.create_text_label("Notes:", 1, 2, "e")
janelaPrincipal.create_horizontal_scale_with_label("Volume :", 0, 100, 20, janelaPrincipal._volume, 200, 0, 1, "nwe")
janelaPrincipal.create_horizontal_scale_with_label("BPM :", 0, 100, 20, janelaPrincipal._bpm, 200, 0, 3, "nwe")
janelaPrincipal.create_combobox(('Piano', 'Guitar', 'Violin', 'Drums'), janelaPrincipal._instrument, 1, 4, "nwe")
janelaPrincipal.create_combobox(('Octave 1', 'Octave 2', 'Octave 3', 'Octave 4'), janelaPrincipal._octave, 1, 5, "nwe")
janelaPrincipal.set_weights(4, 6)
janelaPrincipal.set_paddings(5, 5)

janelaPrincipal.start_mainloop()