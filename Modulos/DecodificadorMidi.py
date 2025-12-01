from SequenciaMidi import SequenciaMidi
from random import choice 

class DecodificadorMidi:
    OFFSET_NOTAS = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'H': 10, 'B': 11}
    NOTAS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    REPETE_OU_TELEFONE = ['I', 'O', 'U']
    BPM_MINIMO = 40
    BPM_MAXIMO = 240
    INST_MINIMO = 0
    INST_MAXIMO = 127
    OITAVA_MINIMA = 0
    OITAVA_MAXIMA = 8
    VOL_MINIMO = 0
    VOL_MAXIMO = 127
    AUMENTO_VELOCITY = 20
    MUDANCA_BPM = 20

    def __init__(self, bpm_padrao : int=100, instrumento_padrao : int=14, oitava_padrao : int=4, volume_padrao : int=60) -> None:
        self.set_instrumento_padrao(instrumento_padrao)
        self.set_oitava_padrao(oitava_padrao)
        self.set_volume_padrao(volume_padrao)
        self.set_bpm_padrao(bpm_padrao)

    def texto_para_sequencia_midi(self, texto : str) -> SequenciaMidi:
        self._inicializa_seq_midi()

        self._decodifica(texto)

        return self._sequencia

    def _decodifica(self, texto : str) -> None:
        # Temos tokens de tamanho 1 e 4. É necessário checar primeiro as maiores.
        i = 0
        while i < len(texto):
            # Tokens de tamanho 4:
            token = texto[i:i+4]
            if token in ['OIT+', 'OIT-', 'BPM+', 'BPM-'] or self._is_token_troca_inst(token):
                self._decodifica_tam_4(token)
                i += 4
            # Tokens de tamanho 1:
            else:
                token = texto[i]
                self._decodifica_tam_1(token)
                i+=1
            self._registra_ultimo_token(token)

    def _decodifica_tam_1(self, token):
        if self._is_nota(token):
            self._tocar_nota(token)
        elif token == ' ': #(espaço)
            self._aumenta_volume()
        elif token == '?':
            self._tocar_aleatoria()
        elif self._is_repete_ou_telefone(token):
            self._repete_nota_ou_telefone()
        elif token == ';':
            self._tocar_pausa()

    def _decodifica_tam_4(self, token) -> None:
        if token == 'OIT+':
            self._aumenta_oitava()
        elif token == 'OIT-':
            self._diminui_oitava()
        elif token == 'BPM+':
            self._aumenta_bpm()
        elif token == 'BPM-':
            self._diminui_bpm()
        else:
            novo_inst = int(token[0:3])
            self._trocar_instrumento(novo_inst)

    def get_bpm_padrao(self) -> int:
        return self._bpm_padrao
   
    def set_bpm_padrao(self, bpm : int) -> None: 
        if self.BPM_MINIMO <= bpm and bpm <= self.BPM_MAXIMO:
            self._bpm_padrao = bpm
        else:
            raise ValueError(f"BPM deve estar entre {self.BPM_MINIMO} e {self.BPM_MAXIMO}.")

    def get_instrumento_padrao(self) -> int:
        return self._instrumento_padrao
   
    def set_instrumento_padrao(self, instrumento : int) -> None:
        if self.INST_MINIMO <= instrumento and instrumento <= self.INST_MAXIMO:
            self._instrumento_padrao = instrumento
        else:
            raise ValueError(f"Instrumento deve estar entre {self.INST_MINIMO} e {self.INST_MAXIMO}.")

    def get_oitava_padrao(self) -> int:
        return self._oitava_padrao
    
    def set_oitava_padrao(self, oitava : int) -> None:
        if self.OITAVA_MINIMA <= oitava and oitava <= self.OITAVA_MAXIMA:
            self._oitava_padrao = oitava
        else:
            raise ValueError(f"Oitava deve estar entre {self.OITAVA_MINIMA} e {self.OITAVA_MAXIMA}.")

    def get_volume_padrao(self) -> int:
        return self._volume_padrao
    
    def set_volume_padrao(self, volume : int) -> None:
        if self.VOL_MINIMO <= volume and volume <= self.VOL_MAXIMO:
            self._volume_padrao = volume
        else:
            raise ValueError(f"Volume deve estar entre {self.VOL_MINIMO} e {self.VOL_MAXIMO}.")
        
    def _inicializa_seq_midi(self) -> None:
        self._sequencia = SequenciaMidi()
        self._timestamp = 0
        self._set_bpm(self.get_bpm_padrao())
        self._instrumento_atual = self.get_instrumento_padrao()
        self._trocar_instrumento(self._instrumento_atual)
        self._set_oitava(self.get_oitava_padrao())
        self._volume = self.get_volume_padrao()
        self._registra_ultimo_token('000\n') 
        # é como se toda sequência iniciasse com uma troca de instrumento
    
    def _oitava_para_nota(self, oitava : int) -> int:
        return oitava * 12 + 12

    def _bpm_para_intervalo_ms(self, bpm : int) -> float:
        if bpm <= 0:
            raise ValueError("BPM não deve ser zero ou negativo!")
        # retorna intervalo entre batidas em milissegundos
        return 60 * 1000 / bpm

    def _incrementa_timestamp(self) -> None:
        self._timestamp += self._intervalo
        
    def _tocar_nota(self, token : str) -> None:
        token_maiusculo = token.upper()
        nota = self._do_oitava + self.OFFSET_NOTAS[token_maiusculo]
        self._sequencia.ativar_nota(nota, self._volume, self._timestamp)
        self._incrementa_timestamp()
        self._sequencia.desativar_nota(nota, self._volume, self._timestamp)

    def _aumenta_volume(self) -> None:
        self._set_volume(self._volume + self.AUMENTO_VELOCITY)

    def _set_volume(self, volume : int) -> None:
        volume_novo = volume
        if volume_novo < self.VOL_MINIMO:
           volume_novo = self.VOL_MINIMO
        elif volume_novo > self.VOL_MAXIMO:
            volume_novo = self.VOL_MAXIMO
        self._volume = volume_novo

    def _set_oitava(self, oitava : int) -> None:
        oitava_nova = oitava
        if oitava_nova < self.OITAVA_MINIMA:
           oitava_nova = self.OITAVA_MINIMA
        elif oitava_nova > self.OITAVA_MAXIMA:
            oitava_nova = self.OITAVA_MAXIMA
        self._oitava = oitava_nova
        self._do_oitava = self._oitava_para_nota(oitava_nova)

    def _aumenta_oitava(self) -> None:
        self._set_oitava(self._oitava + 1)

    def _diminui_oitava(self) -> None:
        self._set_oitava(self._oitava - 1)

    def _set_bpm(self, bpm : int) -> None:
        bpm_novo = bpm
        if bpm_novo < self.BPM_MINIMO:
           bpm_novo = self.BPM_MINIMO
        elif bpm_novo > self.BPM_MAXIMO:
            bpm_novo = self.BPM_MAXIMO
        self._bpm = bpm_novo
        self._intervalo = self._bpm_para_intervalo_ms(bpm_novo)
    
    def _aumenta_bpm(self) -> None:
        self._set_bpm(self._bpm + self.MUDANCA_BPM)
    
    def _diminui_bpm(self) -> None:
        self._set_bpm(self._bpm - self.MUDANCA_BPM)

    def _tocar_pausa(self) -> None:
        self._timestamp += self._intervalo
    
    def _trocar_instrumento(self, inst : int) -> None:
        self._instrumento_atual = inst
        self._sequencia.mudar_instrumento(inst, self._timestamp)

    def _is_token_troca_inst(self, token : str) -> bool:
        # formato 123\n
        return len(token) == 4 and token[3] == '\n' \
            and token[0:2].isdigit() \
            and int(token[0:2]) >= self.INST_MINIMO and int(token[0:2]) <= self.INST_MAXIMO
    
    def _is_repete_ou_telefone(self, token : str) -> bool:
        return token.upper() in self.REPETE_OU_TELEFONE

    def _is_nota(self, token : str) -> bool:
        return token.upper() in self.NOTAS

    def _registra_ultimo_token(self, token : str) -> None:
        if self._is_nota(token) or token == '?':
            self._ultimo_token_eh_nota = True
            self._ultima_nota = token
        elif self._is_repete_ou_telefone(token) and self._ultimo_token_eh_nota:
            self._ultimo_token_eh_nota = True
        else:
            self._ultimo_token_eh_nota = False

    def _repete_nota_ou_telefone(self) -> None:
        INST_TELEFONE = 124
        NOTA_TELEFONE = 'D'
        if self._ultimo_token_eh_nota:
            self._tocar_nota(self._ultima_nota)
        else:
            instrumento_atual = self._instrumento_atual
            self._trocar_instrumento(INST_TELEFONE)
            self._tocar_nota(NOTA_TELEFONE)
            self._trocar_instrumento(instrumento_atual)
    
    def _tocar_aleatoria(self) -> None:
        nota_aleatoria = choice(self.NOTAS)
        self._tocar_nota(nota_aleatoria)
