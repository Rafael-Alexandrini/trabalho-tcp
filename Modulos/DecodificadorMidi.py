from SequenciaMidi import SequenciaMidi

class DecodificadorMidi:
    def __init__(self, instrumento_padrao : int=14, oitava_padrao : int=4, volume_padrao : int=60) -> None:
        self._instrumento_padrao = instrumento_padrao
        self._oitava_padrao = oitava_padrao
        self._volume_padrao = volume_padrao

    def texto_para_sequencia_midi(self, texto : str, bpm : int) -> SequenciaMidi:
        self._sequencia = SequenciaMidi()
        self._timestamp_atual = 0
        self._mudar_instrumento(self._instrumento_padrao)
        
        oitava_atual = self.get_oitava_padrao()

        return self._sequencia
    
    def get_instrumento_padrao(self) -> int:
        return self._instrumento_padrao
   
    def set_instrumento_padrao(self, instrumento : int) -> None:
        self._instrumento_padrao = instrumento

    def get_oitava_padrao(self) -> int:
        return self._oitava_padrao
    
    def set_oitava_padrao(self, oitava : int) -> None:
        self._oitava_padrao = oitava

    def get_volume_padrao(self) -> int:
        return self._volume_padrao
    
    def set_volume_padrao(self, volume : int) -> None:
        self._volume_padrao = volume
    
    def _mudar_instrumento(self, instrumento : int) -> None:
        MUDANCA_INSTRUMENTO = 192
        self._sequencia.anexar_mensagem_midi([MUDANCA_INSTRUMENTO, instrumento, 0], 0)
    
    