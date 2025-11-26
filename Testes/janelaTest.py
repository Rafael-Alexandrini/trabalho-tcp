from Janela import Janela

jp = Janela("Captain MIDI", (10, 10, 10, 10))
text = jp.create_text_widget(50, 10, "C D E F G A B", 2, 1, "we")
play_button = jp.create_button("Play", lambda: print("Play button pressed"), 3, 3, "we")
text_label = jp.create_text_label("Text:", 1, 1, "ne", "Arial 20 bold")
jp.create_text_label("Notes:", 1, 2, "e")
volume_scale = jp.create_horizontal_scale_with_label("Volume :", 0, 100, 20, jp.get_vol_var(), 200, 0, 1, "nwe")
jp.create_horizontal_scale_with_label("BPM :", 0, 100, 20, jp.get_bpm_var(), 200, 0, 3, "nwe")
instrument_box = jp.create_combobox(('Piano', 'Guitar', 'Violin', 'Drums'), jp.get_instrument_var(), 1, 4, "nwe")
octave_box = jp.create_combobox(('1', '2', '3', '4'), jp.get_octave_var(), 1, 5, "nwe")
jp.add_menu_command('Load txt', lambda: print('Load txt file'))
jp.add_menu_command('Save txt', lambda: print('Save txt file'))
jp.add_menu_command('Save MIDI', lambda: print('Save MIDI file'))
jp.set_weights(4, 6)
jp.set_paddings(5, 5)

jp.bind_combobox_event(instrument_box, lambda e: print(f"Selected instrument: {jp.get_instrument_var().get()}"))
jp.bind_combobox_event(octave_box, lambda e: print(f"Selected octave: {jp.get_octave_var().get()}"))

#if (jp.is_text_enabled()):
#    print("Text widget is enabled")
#if( jp.is_widget_enabled(play_button)):
#    print("Play button is enabled")
#
#jp.disable_text()
#jp.disable_widget(play_button)
##jp.disable_widget(volume_scale)
##jp.disable_widget(text_label)
##jp.disable_widget(octave_box)
#
#if not (jp.is_text_enabled()):
#    print("Text widget is disabled")
#if not (jp.is_widget_enabled(play_button)):
#    print("Play button is disabled")

jp.start_mainloop()