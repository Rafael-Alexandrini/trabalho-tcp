from Modulos import TocadorMidi, DecodificadorMidi

meuTocador = TocadorMidi.TocadorMidi()
meuDecod = DecodificadorMidi.DecodificadorMidi()

while True:
    tocar = input("Tocar S ou N ou P: ")
    if tocar == "S":
        file_path = 'Rascunho\\musica.txt'
        with open(file_path, 'r') as file:
            file_content = file.read()
        meuTocador.tocar(meuDecod.texto_para_sequencia_midi(file_content))
    if tocar == "P":
        meuTocador.parar()