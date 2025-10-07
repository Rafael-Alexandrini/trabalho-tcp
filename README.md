# Documentação 

# Classes
## JanelaPrincipal

## TocadorMidi
### `TocadorMidi()`

Instancia um novo TocadorMidi.

### `toca_sequencia_midi(sequencia_midi)`

Toca uma sequência de sinais MIDI pelo output padrão de MIDI do computador.

`sequencia_midi` é uma lista de sinais MIDI com timestamp em segundos. 

O exemplo abaixo instancia um TocadorMidi, cria e toca uma sequência MIDI, equivalente a definir o instrumento como Bright Acoustic Piano (General MIDI #2) e tocar Dó Ré Mi, a 120 BPM:
```python
meu_tocador_midi = TocadorMidi()

sequencia_midi = [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]

meu_tocador_midi.toca_sequencia_midi(sequencia_midi)
```
## DecodificadorMidi
