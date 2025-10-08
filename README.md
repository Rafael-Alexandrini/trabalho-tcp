# Documentação 

# Classes
## JanelaPrincipal

## TocadorMidi

Permite reproduzir e interromper sequências de mensagens MIDI.

### `TocadorMidi()`

Instancia um novo TocadorMidi.

### `tocar_sequencia_midi(sequencia_midi)`

Toca uma sequência de mensagens MIDI pelo output padrão de MIDI do computador.

`sequencia_midi` é uma lista de mensagens MIDI com timestamp em segundos. 

O exemplo abaixo instancia um TocadorMidi, cria e toca uma sequência MIDI, equivalente a definir o instrumento como Bright Acoustic Piano (General MIDI #2) e tocar Dó Ré Mi, a 120 BPM:
```python
meu_tocador_midi = TocadorMidi()

sequencia_midi = [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]

meu_tocador_midi.tocar_sequencia_midi(sequencia_midi)
```

### `parar_sequencia_midi()`

Para a reprodução da sequência MIDI

## DecodificadorMidi

Permite a tradução de texto em sequências de mensagens MIDI, de acordo com a tabela abaixo:
### Tabela de equivalência

| Caractere | Efeito |
| ------ | ----------- |
| A   | Toca a nota Lá a partir da oitava atual|
| B   | Toca a nota Si a partir da oitava atual|
| C   | Toca a nota Dó a partir da oitava atual|
| D   | Toca a nota Ré a partir da oitava atual|
| E   | Toca a nota Mi a partir da oitava atual|
| F   | Toca a nota Fá a partir da oitava atual|
| G   | Toca a nota Sol a partir da oitava atual|
| H   | Toca a nota Si Bemol a partir da oitava atual|
| a, b, c, d, e, f, g, h   | Pausa (silêncio)|
| Ponto de exclamação (!)| Muda instrumento para #24 Bandoneon|
| I, i, O, o, U, u| Muda instrumento para #110 Gaita de Foles|
| Nova linha| Muda instrumento para #123 Ondas do Mar|
| Ponto e vírgula (;) ou dígito ímpar| Muda instrumento para #15 Tubular Bells|
| Vírgula (,)| Muda instrumento para #114 Agogô|
| Ponto de interrogação (?) e Ponto (.)| Aumenta a oitava, resetando no limite|
|Espaço |Aumenta o volume, parando no limite máximo|
|Outros caracteres|Repete nota ou pausa anterior|

 Note que cada nota ou pausa é efetuada pela duração de uma batida.

 Note também que o número correspondente aos instrumentos é indexado em 1, mas seus valores são indexados em 0. Ou seja, o 24º instrumento, o Bandoneon, tem código 23.

### `DecodificadorMidi(intrumento_padrao=14, oitava_padrao=60, volume_padrao=80)`
Instancia um DecodificadorMidi. 
É possível passar configurações iniciais personalizadas: 

Os três parâmetros são inteiros de 0 a 127.

`instrumento_padrao` corresponde ao instrumento do padrão GeneralMIDI com o qual a sequência MIDI vai iniciar. 

`oitava_padrao` indica a nota que será considerada como o Dó Central no início da sequência MIDI. Deve-se passar múltiplos de 12 para corresponder ao Dó de cada oitava.

`volume_padrao` indica a velocity inicial da sequência MIDI.

### `texto_para_sequencia_midi(texto, bpm)`
Retorna uma sequência MIDI (uma lista de mensagens MIDI com timestamp em segundos), criada através da decodificação do `texto` e `bpm` conforme a tabela.

Exemplo:
```python
meu_decodificador = DecodificadorMidi(instrumento_padrao=1, volume_padrao=100)

sequencia_midi = meu_decodificador.texto_para_sequencia_midi("CDE", 120)

print(sequencia_midi)

// Output: 
// [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]
```