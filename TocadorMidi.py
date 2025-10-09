import pygame.midi
from SequenciaMidi import SequenciaMidi
from threading import Timer
import copy

class TocadorMidi:
    def __init__(self) -> None:
        self.reproduzindo = False
        self._inicia_saida_midi()

    def tocar_sequencia_midi(self, sequencia_midi : SequenciaMidi, comando_final_seq=None) -> None:
        if self.reproduzindo is True:
            return
        self.reproduzindo = True

        lista_midi = copy.deepcopy(sequencia_midi.get_lista_mensagens_midi())
        
        tempo_fim_musica = self._get_tempo_fim_da_musica(lista_midi)
        
        lista_midi = self._ajustar_timestamp_lista_midi(lista_midi)
        
        if comando_final_seq is not None:
            timer_chamar_funcao = Timer(tempo_fim_musica, self._chama_func_fim_da_musica, args=[comando_final_seq])
            timer_chamar_funcao.start()

        self.saida_midi.write(lista_midi)

    def parar_sequencia_midi(self) -> None:
        if self.reproduzindo is True:
            self.saida_midi.abort()
            del self.saida_midi
            pygame.midi.quit()

            self.reproduzindo = False

            self._inicia_saida_midi()

    def sair(self) -> None:
        self.saida_midi.abort()
        del self.saida_midi
        pygame.midi.quit()

    def _ajustar_timestamp_lista_midi(self, lista_midi : list) -> list:
        tempo_atual = pygame.midi.time()

        for msg_e_time in lista_midi:
            msg_e_time[1] += tempo_atual 
              
        return lista_midi
        
    def _get_tempo_fim_da_musica(self, lista_midi : list) -> int:
        tempo_caso_de_erro = 0
        if len(lista_midi) == 0:
            return tempo_caso_de_erro
        
        ultima_mensagem = lista_midi[-1]

        if len(ultima_mensagem) != 2:
            return tempo_caso_de_erro
        
        tempo_ms = ultima_mensagem[1]
        return tempo_ms / 1000

    def _chama_func_fim_da_musica(self, comando_final_seq) -> None:
        if self.reproduzindo is True:
            self.reproduzindo = False
            comando_final_seq()

    def _inicia_saida_midi(self) -> None:
        pygame.midi.init()        
        id_saida_midi_padrao = pygame.midi.get_default_output_id()
        print("Saída:", id_saida_midi_padrao)
        print(pygame.midi.get_device_info(id_saida_midi_padrao))
        latencia_recomendada = 10
        self.saida_midi = pygame.midi.Output(id_saida_midi_padrao, latency=latencia_recomendada)

