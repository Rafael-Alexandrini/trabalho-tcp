from Modulos.DecodificadorMidi import DecodificadorMidi
from Modulos.SequenciaMidi import SequenciaMidi
import pytest


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


    

    
        