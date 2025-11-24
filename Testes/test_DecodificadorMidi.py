from Modulos.DecodificadorMidi import DecodificadorMidi
from Modulos.SequenciaMidi import SequenciaMidi
import pytest

def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n


@pytest.fixture()
def decodificador_base():
    bpm, inst, oitava, volume = 120, 1, 4, 60
    decoder = DecodificadorMidi(bpm, inst, oitava, volume)
    return decoder, bpm, inst, oitava, volume

def test_decodificaC(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_decodificaH(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    si_bemol = do_oitava + 10
    sequencia_saida = decoder.texto_para_sequencia_midi("H")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(si_bemol, volume, 0)
    sequencia_esperada.desativar_nota(si_bemol, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_muda_dados_padrao(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    bpm_novo = bpm + 10
    inst_novo = (inst + 10) % 128
    oitava_nova = (oitava + 1) % 9
    volume_novo = (volume + 10) % 128 
    decoder.set_bpm_padrao(bpm_novo)
    decoder.set_instrumento_padrao(inst_novo)
    decoder.set_oitava_padrao(oitava_nova)
    decoder.set_volume_padrao(volume_novo)
    assert decoder.get_bpm_padrao() == bpm_novo
    assert decoder.get_instrumento_padrao() == inst_novo
    assert decoder.get_oitava_padrao() == oitava_nova
    assert decoder.get_volume_padrao() == volume_novo

def test_aumenta_volume(decodificador_base):
    # Considera-se "Dobrar o volume" aumentar em vinte
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12

    volume_teste = 60
    decoder.set_volume_padrao(volume_teste)
    volume_novo = 80 

    sequencia_saida = decoder.texto_para_sequencia_midi(" C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume_novo, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume_novo, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_aumenta_volume_limite(decodificador_base):
    # Considera-se "Dobrar o volume" aumentar em vinte
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12

    volume_teste = 120
    decoder.set_volume_padrao(volume_teste)
    volume_novo = 127 

    sequencia_saida = decoder.texto_para_sequencia_midi(" C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume_novo, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume_novo, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_aumenta_oitava(decodificador_base):
    # Oitavas vão de 0 até 8 (midi 12 até 106)
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    oitava_teste = 4
    decoder.set_oitava_padrao(oitava_teste)
    do_oitava = 12 * oitava_teste + 12
    do_oitava_incrementado = do_oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("OIT+C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava_incrementado, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava_incrementado, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()
        
def test_aumenta_oitava_limite(decodificador_base):
    # Oitavas vão de 0 até 8 (midi 12 até 106)
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    oitava_teste = 8
    decoder.set_oitava_padrao(oitava_teste)
    do_oitava = 12 * oitava_teste + 12
    do_oitava_incrementado = do_oitava
    sequencia_saida = decoder.texto_para_sequencia_midi("OIT+C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava_incrementado, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava_incrementado, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_diminui_oitava(decodificador_base):
    # Oitavas vão de 0 até 8 (midi 12 até 106)
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    oitava_teste = 4
    decoder.set_oitava_padrao(oitava_teste)
    do_oitava = 12 * oitava_teste + 12
    do_oitava_decrementado = do_oitava - 12
    sequencia_saida = decoder.texto_para_sequencia_midi("OIT-C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava_decrementado, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava_decrementado, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_diminui_oitava_limite(decodificador_base):
    # Oitavas vão de 0 até 8 (midi 12 até 106)
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    oitava_teste = 0
    decoder.set_oitava_padrao(oitava_teste)
    do_oitava = 12 * oitava_teste + 12
    do_oitava_decrementado = do_oitava
    sequencia_saida = decoder.texto_para_sequencia_midi("OIT+C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava_decrementado, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava_decrementado, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_vogal_repete(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("Cu") # é ESSENCIAL que a vogal testada seja u :)
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    sequencia_esperada.ativar_nota(do_oitava, volume, intervalo_ms) # repete a nota
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms * 2)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_vogal_nao_repete(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("C uC") # é ESSENCIAL que a vogal testada seja u :)
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    volume_aumentado = clamp(volume + 20, 0, 127) # espaço aumenta volume, aqui só pra não ser uma nota
    # char anterior não é nota, então toca telefone
    sequencia_esperada.mudar_instrumento(124, 0)
    sequencia_esperada.ativar_nota(62, volume_aumentado, intervalo_ms)
    sequencia_esperada.desativar_nota(62, volume_aumentado, intervalo_ms*2)
    # tem que trocar o instrumento de volta
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume_aumentado, intervalo_ms*3) 
    sequencia_esperada.desativar_nota(do_oitava, volume_aumentado, intervalo_ms*4)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_nova_linha(decodificador_base):
    # Troca de instrumento: nova linha com números depois altera instrumento para o número escrito
    # se não houverem números, não altera o instrumento
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("C\n020C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    sequencia_esperada.mudar_instrumento(20, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, intervalo_ms*2)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms*3)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_bpm_mais(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    bpm_teste = 100
    decoder.set_bpm_padrao(bpm_teste)
    intervalo_ms = 60 * 1000 / (bpm_teste + 20)
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("BPM+C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_bpm_mais_limite(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    bpm_teste = 235
    decoder.set_bpm_padrao(bpm_teste)
    intervalo_ms = 60 * 1000 / (240)
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("BPM+C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_bpm_menos(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    bpm_teste = 140
    decoder.set_bpm_padrao(bpm_teste)
    intervalo_ms = 60 * 1000 / (bpm_teste - 20)
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("BPM-C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_bpm_menos_limite(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    bpm_teste = 45
    decoder.set_bpm_padrao(bpm_teste)
    intervalo_ms = 60 * 1000 / (40)
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("BPM-C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_ponto_e_virgula(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("C;C")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    # pausa de intervalo_ms até intervalo_ms*2
    sequencia_esperada.ativar_nota(do_oitava, volume, intervalo_ms*2)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms*3)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()
"""
def test_ponto(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("C..")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    # um ponto: intervalo_ms até intervalo_ms*2
    # dois pontos: intervalo_ms*2 até intervalo_ms*3
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms*3)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()
"""
def test_outro_char(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    intervalo_ms = 60 * 1000 / bpm
    do_oitava = 12 * oitava + 12
    sequencia_saida = decoder.texto_para_sequencia_midi("pppCpppp")
    sequencia_esperada = SequenciaMidi()
    sequencia_esperada.mudar_instrumento(inst, 0)
    sequencia_esperada.ativar_nota(do_oitava, volume, 0)
    sequencia_esperada.desativar_nota(do_oitava, volume, intervalo_ms)
    assert sequencia_saida.get_lista_mensagens_midi() == sequencia_esperada.get_lista_mensagens_midi()

def test_set_oitava_invalida(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    oitava_nova = 100
    with pytest.raises(ValueError):
        decoder.set_oitava_padrao(oitava_nova)
        
def test_set_bpm_invalido(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    bpm_novo = 0
    with pytest.raises(ValueError):
        decoder.set_bpm_padrao(bpm_novo)

def test_set_instrumento_invalido_menor(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    inst_novo = -1
    with pytest.raises(ValueError):
        decoder.set_instrumento_padrao(inst_novo)

def test_set_instrumento_invalido_limite(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    inst_novo = 128
    with pytest.raises(ValueError):
        decoder.set_instrumento_padrao(inst_novo)
        
def test_set_volume_invalido_menor(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    vol_novo = -1
    with pytest.raises(ValueError):
        decoder.set_volume_padrao(vol_novo)

def test_set_volume_invalido_limite(decodificador_base):
    decoder, bpm, inst, oitava, volume = decodificador_base
    vol_novo = 128
    with pytest.raises(ValueError):
        decoder.set_volume_padrao(vol_novo)