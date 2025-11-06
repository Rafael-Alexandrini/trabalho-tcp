from typing import Union

class SequenciaMidi:
    def __init__(self) -> None:
        self._lista_midi = []

    def get_lista_mensagens_midi(self) -> list:
        return self._lista_midi
    
    def anexar_mensagem_midi(self, mensagem_midi : list[int], timestamp : float) -> None:
        self._check_timestamp(timestamp)
        self._lista_midi.append([mensagem_midi, timestamp])

    def anexar_varias_mensagens_midi(self, lista_msg_e_tempos : list[list]) -> None:
        for mensagem in lista_msg_e_tempos:
            self.anexar_mensagem_midi(mensagem[0], mensagem[1])

    def ativar_nota(self, nota : int, velocity : int, timestamp : float) -> None:
        ATIVAR_NOTA = 144
        self.anexar_mensagem_midi([ATIVAR_NOTA, nota, velocity], timestamp)

    def desativar_nota(self, nota : int, velocity : int, timestamp : float) -> None:
        DESATIVAR_NOTA = 128
        self.anexar_mensagem_midi([DESATIVAR_NOTA, nota, velocity], timestamp)

    def mudar_instrumento(self, instrumento : int, timestamp : float) -> None:
        MUDAR_INSTRUMENTO = 192
        self.anexar_mensagem_midi([MUDAR_INSTRUMENTO, instrumento, 0], timestamp)

    def get_tempo_fim_musica_ms(self) -> float:
        if len(self._lista_midi) == 0:
            return 0
        ultima_mensagem = self._lista_midi[-1]
        return ultima_mensagem[1]

    def get_tempo_fim_musica_s(self) -> float:
        tempo_ms = self.get_tempo_fim_musica_ms()
        MILISEGUNDOS_POR_SEGUNDO = 1000
        return tempo_ms / MILISEGUNDOS_POR_SEGUNDO
    
    def _check_timestamp(self, timestamp : float):
        if timestamp < 0:
            raise ValueError("Timestamps devem ser positivos!")
        if timestamp < self.get_tempo_fim_musica_ms():
            raise ValueError("Timestamps devem estar em ordem!")
    