class SequenciaMidi:
    def __init__(self) -> None:
        self.lista_midi = []

    def get_lista_mensagens_midi(self) -> list:
        return self.lista_midi
    
    def anexar_mensagem_midi(self, mensagem_midi, timestamp) -> None:
        self.lista_midi.append([mensagem_midi, timestamp])

    def anexar_varias_mensagens_midi(self, lista_msg_e_tempos) -> None:
        self.lista_midi.extend(lista_msg_e_tempos)

