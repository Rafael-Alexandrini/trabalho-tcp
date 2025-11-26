from .SequenciaMidi import SequenciaMidi
from random import choice 

class DecodificadorMidi:
    def __init__(self, bpm_padrao : int=100, instrumento_padrao : int=14, oitava_padrao : int=4, volume_padrao : int=60) -> None:
        self._instrumento_padrao = instrumento_padrao
        self._oitava_padrao = oitava_padrao
        self._volume_padrao = volume_padrao
        self._bpm_padrao = bpm_padrao

    def texto_para_sequencia_midi(self, texto : str) -> SequenciaMidi:
        self._sequencia = SequenciaMidi()
        self._timestamp = 0
        self._set_bpm(self.get_bpm_padrao())
        self._instrumento_atual = self.get_instrumento_padrao()
        self._trocar_instrumento(self._instrumento_atual)
        self._set_oitava(self.get_oitava_padrao())
        self._volume = self.get_volume_padrao()
        self._registra_ultimo_token('000\n')
        
        
        parser = texto 
        i = 0
        while i < len(texto):   # enquanto houver elementos na lista
            token = parser[i:i+4]
            if token == 'OIT+':
                self._aumenta_oitava()
                i+=3
            elif token == 'OIT-':
                self._diminui_oitava()
                i+=3
            elif token == 'BPM+':
                self._aumenta_bpm()
                i+=3
            elif token == 'BPM-':
                self._diminui_bpm()
                i+=3
            elif self._is_token_troca_inst(token):
            # token é no formato 123\n 
                self._trocar_instrumento(int(token[0:3]))
                i+=3
            else:
                token = parser[i]
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
           
            i+=1

            self._registra_ultimo_token(token)

        return self._sequencia

   
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
        
    # FUNÇÕES AUXILIARES PARA A DECODIFICAÇÃO
    
    def _oitava_para_nota(self, oitava : int) -> int:
        return oitava * 12 + 12

    def _bpm_para_intervalo_ms(self, bpm : int) -> float:
        if bpm <= 0:
            raise ValueError("BPM não deve ser zero ou negativo!")
        # retorna intervalo entre batidas em milissegundos
        return 60 * 1000 / bpm

    def _incrementa_timestamp(self):
        self._timestamp += self._intervalo
        
    def _tocar_nota(self, token : str) -> None:
        token_maiusculo = token.upper()
        offset_nota = {
            'C': 0,  
            'D': 2,
            'E': 4,
            'F': 5,
            'G': 7,
            'A': 9,
            'H': 10,
            'B': 11,
            }
        nota = self._do_oitava + offset_nota[token_maiusculo]
        self._sequencia.ativar_nota(nota, self._volume, self._timestamp)
        self._incrementa_timestamp()
        self._sequencia.desativar_nota(nota, self._volume, self._timestamp)

    def _aumenta_volume(self) -> None:
        AUMENTO_VELOCITY = 20
        self._set_volume(self._volume + AUMENTO_VELOCITY)


    def _set_volume(self, volume : int) -> None:
        MINIMO_VELOCITY = 0
        MAXIMO_VELOCITY = 127
        volume_novo = volume
        if volume_novo < MINIMO_VELOCITY:
           volume_novo = MINIMO_VELOCITY
        elif volume_novo > MAXIMO_VELOCITY:
            volume_novo = MAXIMO_VELOCITY
        self._volume = volume_novo

    def _set_oitava(self, oitava : int) -> None:
        MINIMO_OITAVA = 0
        MAXIMO_OITAVA = 8
        oitava_nova = oitava
        if oitava_nova < MINIMO_OITAVA:
           oitava_nova = MINIMO_OITAVA
        elif oitava_nova > MAXIMO_OITAVA:
            oitava_nova = MAXIMO_OITAVA
        self._oitava = oitava_nova
        self._do_oitava = self._oitava_para_nota(oitava_nova)

    def _aumenta_oitava(self) -> None:
        self._set_oitava(self._oitava + 1)

    def _diminui_oitava(self) -> None:
        self._set_oitava(self._oitava - 1)

    def _set_bpm(self, bpm : int) -> None:
        MINIMO_BPM = 40
        MAXIMO_BPM = 240
        bpm_novo = bpm
        if bpm_novo < MINIMO_BPM:
           bpm_novo = MINIMO_BPM
        elif bpm_novo > MAXIMO_BPM:
            bpm_novo = MAXIMO_BPM
        self._bpm = bpm_novo
        self._intervalo = self._bpm_para_intervalo_ms(bpm_novo)
    
    def _aumenta_bpm(self) -> None:
        AUMENTO_BPM = 20
        self._set_bpm(self._bpm + AUMENTO_BPM)
    
    def _diminui_bpm(self) -> None:
        DECREMENTO_BPM = 20
        self._set_bpm(self._bpm - DECREMENTO_BPM)

    def _tocar_pausa(self) -> None:
        self._timestamp += self._intervalo
    
    def _trocar_instrumento(self, inst : int) -> None:
        self._instrumento_atual = inst
        self._sequencia.mudar_instrumento(inst, self._timestamp)

    def _is_token_troca_inst(self, token : str) -> bool:
        # formato 123\n
        MAXIMO_INSTRUMENTO = 127
        MINIMO_INSTRUMENTO = 0
        return len(token) == 4 and token[3] == '\n' \
            and token[0:2].isnumeric() \
            and int(token[0:2]) >= MINIMO_INSTRUMENTO and int(token[0:2]) <= MAXIMO_INSTRUMENTO
    
    def _is_repete_ou_telefone(self, token : str) -> bool:
        return token.upper() in ['I', 'O', 'U']

    def _is_nota(self, token : str) -> bool:
        return token.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

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
        nota_aleatoria = choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        self._tocar_nota(nota_aleatoria)
