from Modulos import TocadorMidi, DecodificadorMidi

meuTocador = TocadorMidi.TocadorMidi()
meuDecod = DecodificadorMidi.DecodificadorMidi()

while True:
    texto = input("Digite algo: ")
    seq = meuDecod.texto_para_sequencia_midi(texto)
    print(seq.get_lista_mensagens_midi())
    meuTocador.tocar(seq)
