import pygame.midi
from SequenciaMidi import SequenciaMidi
from threading import Timer
import copy

class TocadorMidi:
    def __init__(self) -> None:
        self._reproduzindo = False
        self._inicia_saida_midi()

    def tocar(self, musica : SequenciaMidi, comando_fim_musica=None) -> None:
        if self._reproduzindo is True:
            return
        self._reproduzindo = True

        sequencia_midi = copy.deepcopy(musica)

        lista_midi = copy.deepcopy(sequencia_midi.get_lista_mensagens_midi())
        
        lista_midi = self._ajustar_timestamp_lista_midi(lista_midi)
        
        tempo_fim_musica = sequencia_midi.get_tempo_fim_musica_s()
        
        
        timer_chamar_funcao = Timer(tempo_fim_musica, self._chama_func_fim_da_musica, args=[comando_fim_musica])
        timer_chamar_funcao.start()

        self.saida_midi.write(lista_midi)

    def parar(self) -> None:
        if self._reproduzindo is True:
            self._sai_saida_midi()

            self._reproduzindo = False

            self._inicia_saida_midi()

    def sair(self) -> None:
        self._sai_saida_midi()

    def get_reproduzindo(self) -> bool:
        return self._reproduzindo

    def _ajustar_timestamp_lista_midi(self, lista_midi : list) -> list:
        tempo_atual = pygame.midi.time()

        for msg_e_time in lista_midi:
            msg_e_time[1] += tempo_atual 
              
        return lista_midi

    def _chama_func_fim_da_musica(self, comando_final_seq) -> None:
        if self._reproduzindo is True:
            self._reproduzindo = False
            if comando_final_seq is not None:
                comando_final_seq()

    def _inicia_saida_midi(self) -> None:
        pygame.midi.init()        
        id_saida_midi_padrao = pygame.midi.get_default_output_id()   
        latencia_recomendada = 10
        self.saida_midi = pygame.midi.Output(id_saida_midi_padrao, latency=latencia_recomendada)

    def _sai_saida_midi(self):
        self.saida_midi.abort()
        del self.saida_midi
        pygame.midi.quit()
