from Modulos.SequenciaMidi import SequenciaMidi
import pytest

def test_anexar_mensagem_midi():
    seq = SequenciaMidi()
    seq.anexar_mensagem_midi([192, 1, 0], 100)
    assert seq.get_lista_mensagens_midi() == [[[192, 1, 0], 100]]

def test_anexar_ordem_errada():
    seq = SequenciaMidi()
    seq.anexar_mensagem_midi([192, 1, 0], 100)
    with pytest.raises(ValueError):
        seq.anexar_mensagem_midi([144, 60, 100], 0)

def test_anexar_timestamp_negativo():
    seq = SequenciaMidi()
    seq.anexar_mensagem_midi([192, 1, 0], 100)
    with pytest.raises(ValueError):
        seq.anexar_mensagem_midi([144, 60, 100], -50)

def test_anexar_varias_mensagens_midi():
    seq = SequenciaMidi()
    seq.anexar_varias_mensagens_midi([[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500]])
    assert seq.get_lista_mensagens_midi() == [[[192, 1, 0], 0], [[144, 60, 100], 0], [[128, 60, 100], 500]]

def test_anexar_varias_ordem_errada():
    seq = SequenciaMidi()
    with pytest.raises(ValueError):
        seq.anexar_varias_mensagens_midi([[[192, 1, 0], 100], [[144, 60, 100], 0], [[128, 60, 100], 0]])

def test_ativar_nota():
    seq = SequenciaMidi()
    seq.ativar_nota(60, 100, 0)
    seq.ativar_nota(62, 100, 500)
    seq.ativar_nota(64, 100, 1000)
    assert seq.get_lista_mensagens_midi() == [[[144, 60, 100], 0], [[144, 62, 100], 500], [[144, 64, 100], 1000]]

def test_desativar_nota():
    seq = SequenciaMidi()
    seq.desativar_nota(60, 100, 0)
    seq.desativar_nota(62, 100, 500)
    seq.desativar_nota(64, 100, 1000)
    assert seq.get_lista_mensagens_midi() == [[[128, 60, 100], 0], [[128, 62, 100], 500], [[128, 64, 100], 1000]]

def test_mudar_instrumento():
    seq = SequenciaMidi()
    seq.mudar_instrumento(0, 0)
    seq.mudar_instrumento(10, 500)
    seq.mudar_instrumento(127, 1000)
    assert seq.get_lista_mensagens_midi() == [[[192, 0, 0], 0], [[192, 10, 0], 500], [[192, 127, 0], 1000]]
