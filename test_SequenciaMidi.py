from SequenciaMidi import SequenciaMidi
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

