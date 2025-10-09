# Documentação CaptainMIDI
## CaptainMIDI yeah 🤟
CaptainMIDI permite criar e reproduzir músicas por meio de texto. 

O usuário terá acesso a uma interface gráfica, na qual poderá digitar em uma caixa de texto, definir o número de batidas por minuto e apertar em botões Tocar para escutar a música e Parar para deixar de escutar a música. A transformação do texto em música segue o mapeamento apresentado na classe DecodificadorMidi.
# Classes
## SequenciaMidi
Empacotamento de uma lista de mensagens MIDI e seus respectivos timestamps. 

O seguinte exemplo mostra uma sequência de mensagens MIDI equivalentes a definir o instrumento como Bright Acoustic Piano (General MIDI #2) e tocar Dó Ré Mi, com velocity a 100 e BPM a 120.
```python
sequencia_midi = [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]
```
### `SequenciaMidi()`
Instancia uma nova SequenciaMidi vazia.


### `get_lista_mensagens_midi()`
Retorna a lista de mensagens MIDI e timestamps.

### `anexar_mensagem_midi(mensagem_midi, timestamp)`
Ao final da sequência de mensagens MIDI atual, adiciona uma nova mensagem MIDI e timestamp.
`mensagem_midi` é uma lista de três elementos: um de status e dois de dados, conforme a especificação MIDI.
`timestamp` é o tempo, em milisegundos, em que a mensagem será 'tocada' a partir da reprodução da sequência.

### `anexar_varias_mensagens_midi(lista_msg_e_tempos)`
Cada mensagem MIDI e timestamp são adicionados ao final da sequência.



## TocadorMidi

Permite tocar uma SequenciaMidi através da saída de MIDI padrão do computador e também parar essa reprodução.

### `TocadorMidi()`

Instancia um novo TocadorMidi.

### `tocar_sequencia_midi(sequencia_midi, comando_final_seq=None)`

Toca uma sequência de mensagens MIDI pelo output padrão de MIDI do computador.

`sequencia_midi` é uma SequenciaMidi.
`comando_final_seq` é uma função que será chamada quando a sequência MIDI terminar de ser executada, sem contar `parar_sequencia_midi()`.

O exemplo abaixo instancia um TocadorMidi, cria e toca uma SequenciaMidi, equivalente a definir o instrumento como Bright Acoustic Piano (General MIDI #2) e tocar Dó Ré Mi, a 120 BPM:
```python
meu_tocador_midi = TocadorMidi()

sequencia_midi = SequenciaMidi()
sequencia_midi.anexar_varias_mensagens_midi([[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]])

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

`oitava_padrao` indica qual a oitava inicial. Valores inteiros de 0 a 8, sendo 4 o dó central. Obs.: algumas notas podem não emitir som se forem muito graves ou agúdas.

`volume_padrao` indica a velocity inicial da sequência MIDI.

### `texto_para_sequencia_midi(texto, bpm)`
Retorna uma SequenciaMidi, criada através da decodificação do `texto` e `bpm` conforme a tabela.

O exemplo abaixo instancia um DecodificadorMidi com instrumento padrão Bright Acoustic Piano (General MIDI #2), volume padrão 100 e mostra o resultado de traduzir 'CDE' (Dó Ré Mi) para uma sequência MIDI:
```python
meu_decodificador = DecodificadorMidi(instrumento_padrao=1, volume_padrao=100)

sequencia_midi = meu_decodificador.texto_para_sequencia_midi("CDE", 120)

print(sequencia_midi.get_lista_mensagens_midi())

// Output: 
// [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500.0], [[144, 62, 100], 500.0], [[128, 62, 100], 1000.0], [[144, 64, 100], 1000.0], [[128, 64, 100], 1500.0]]
```
### `get_instrumento_padrao()`
### `get_oitava_padrao()`
### `get_volume_padrao()`
### `set_instrumento_padrao(codigo_instrumento)`
### `set_oitava_padrao(oitava)`
### `set_volume_padrao(velocity)`

## JanelaPrincipal
Interface gráfica com o usuário. 

Quando instanciada, gera uma janela com entrada de texto, botões e texto e cria um TocadorMidi e um DecodificadorMidi
### `JanelaPrincipal()`
Instancia a JanelaPrincipal.
### `iniciar()`
Inicia o loop principal da interface.
### `sair()`
Encerra corretamente a interface e o TocadorMidi

### Métodos internos para responder à entrada do usuário:
### `_botao_tocar_pressionado()`
Chamado quando o botão Tocar é pressionado. Gera uma SequenciaMidi correspondente ao texto inserido pelo usuário através do DecodificadorMidi e o toca usando o TocadorMidi. Além disso, altera o botão Tocar para o botão Parar.

### `_botao_parar_pressionado()`
Chamado quando o botão Parar é pressionado. Interrompe a reprodução da música do TocadorMidi e troca o botão Parar pelo o botão Tocar.

### `_musica_acabou()`
Chamado quando a música termina de tocar naturalmente (botão Parar não é pressionado). Troca o botão Parar pelo botão Tocar.

### `_texto_alterado()`
Chamado quando o texto da caixa de entrada de texto é alterado. Se não há texto, bloqueia o botão Tocar. Se há texto, desbloqueia o botão Tocar.


## EntryNumerico
Componente de entrada de valores numéricos: possui campo para digitar e botões para incrementar ou decrementar.
### `EntryNumerico()`
Inicializa um EntryNumerico.
### `get()`
Retorna valor numérico.
### `set(num)`
Define o valor numérico como `num`.