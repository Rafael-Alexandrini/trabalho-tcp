from Modulos.SequenciaMidi import SequenciaMidi

class DecodificadorMidi:
    def __init__(self, bpm_padrao : int=100, instrumento_padrao : int=14, oitava_padrao : int=4, volume_padrao : int=60) -> None:
        self._instrumento_padrao = instrumento_padrao
        self._oitava_padrao = oitava_padrao
        self._volume_padrao = volume_padrao
        self._bpm_padrao = bpm_padrao

    def texto_para_sequencia_midi(self, texto : str) -> SequenciaMidi:
        sequencia = SequenciaMidi()
        timestamp = 0
        intervalo = self._bpm_para_intervalo_ms(self.get_bpm_padrao())
        sequencia.mudar_instrumento(self.get_instrumento_padrao(), timestamp)
        oitava = self.get_oitava_padrao()
        do_oitava = self._oitava_para_nota(self.get_oitava_padrao())
        volume = self.get_volume_padrao()
        




        
        return sequencia
    
    def get_bpm_padrao(self) -> int:
        return self._bpm_padrao
   
    def set_bpm_padrao(self, bpm : int) -> None: 
        BPM_MINIMO = 40
        BPM_MAXIMO = 240
        if BPM_MINIMO <= bpm and bpm <= BPM_MAXIMO:
            self._bpm_padrao = bpm
        else:
            raise ValueError(f"BPM deve estar entre {BPM_MINIMO} e {BPM_MAXIMO}.")

    def get_instrumento_padrao(self) -> int:
        return self._instrumento_padrao
   
    def set_instrumento_padrao(self, instrumento : int) -> None:
        INST_MINIMO = 0
        INST_MAXIMO = 127
        if INST_MINIMO <= instrumento and instrumento <= INST_MAXIMO:
            self._instrumento_padrao = instrumento
        else:
            raise ValueError(f"Instrumento deve estar entre {INST_MINIMO} e {INST_MAXIMO}.")
        

    def get_oitava_padrao(self) -> int:
        return self._oitava_padrao
    
    def set_oitava_padrao(self, oitava : int) -> None:
        OITAVA_MINIMA = 0
        OITAVA_MAXIMA = 8
        if OITAVA_MINIMA <= oitava and oitava <= OITAVA_MAXIMA:
            self._oitava_padrao = oitava
        else:
            raise ValueError(f"Oitava deve estar entre {OITAVA_MINIMA} e {OITAVA_MAXIMA}.")

    def get_volume_padrao(self) -> int:
        return self._volume_padrao
    
    def set_volume_padrao(self, volume : int) -> None:
        VOL_MINIMO = 0
        VOL_MAXIMO = 127
        if VOL_MINIMO <= volume and volume <= VOL_MAXIMO:
            self._volume_padrao = volume
        else:
            raise ValueError(f"Volume deve estar entre {VOL_MINIMO} e {VOL_MAXIMO}.")
        
    
    def _oitava_para_nota(self, oitava : int) -> int:
        return oitava * 12 + 12

    def _bpm_para_intervalo_ms(self, bpm : int) -> float:
        if bpm <= 0:
            raise ValueError("BPM não deve ser zero ou negativo!")
        # retorna intervalo entre batidas em milissegundos
        return 60 * 1000 / bpm
    