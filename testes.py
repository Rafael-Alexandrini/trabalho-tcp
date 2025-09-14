import pygame
import pygame.midi
import time

def tocar_nota_midi():
    """
    Um exemplo completo que inicializa o pygame.midi, seleciona um dispositivo,
    um instrumento e toca uma única nota.
    """
    # Inicializações
    pygame.init()
    pygame.midi.init()

    # --- Seleção do Dispositivo de Saída ---
    print("Dispositivos MIDI de saída disponíveis:")
    output_devices = []
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        if info[3] == 1:  # Verifica se é um dispositivo de saída
            print(f"ID: {i}, Nome: {info[1].decode('utf-8')}")
            output_devices.append(i)

    if not output_devices:
        print("Nenhum dispositivo de saída MIDI encontrado.")
        pygame.midi.quit()
        pygame.quit()
        return

    device_id = pygame.midi.get_default_output_id()
    if device_id not in output_devices:
        # Se o padrão não for um dispositivo de saída válido, pega o primeiro da lista
        device_id = output_devices[0] if output_devices else -1

    try:
        user_input = input(f"Digite o ID do dispositivo de saída (padrão: {device_id}): ")
        if user_input:
            device_id = int(user_input)
            if device_id not in output_devices:
                print("ID inválido. Usando o dispositivo padrão.")
                device_id = pygame.midi.get_default_output_id()

    except ValueError:
        print("Entrada inválida. Usando o dispositivo padrão.")

    if device_id == -1:
        print("Não foi possível selecionar um dispositivo de saída MIDI.")
        pygame.midi.quit()
        pygame.quit()
        return

    print(f"\nUsando o dispositivo com ID: {device_id}")

    # --- Configuração e Execução ---
    midi_output = pygame.midi.Output(device_id)

    # Define o instrumento (0 = Piano)
    instrumento_id = 0
    midi_output.set_instrument(instrumento_id)
    print(f"Instrumento definido como: Piano (ID {instrumento_id})")

    # Parâmetros da nota
    nota_a_tocar = 60  # Dó Central (C4)
    velocidade = 127   # Volume máximo

    try:
        print(f"\nTocando a nota {nota_a_tocar} por 2 segundos...")
        midi_output.note_on(nota_a_tocar, velocity=velocidade)
        time.sleep(2)
        midi_output.note_off(nota_a_tocar, velocity=velocidade)
        print("Execução finalizada.")

    finally:
        # --- Limpeza ---
        del midi_output
        pygame.midi.quit()
        pygame.quit()

if __name__ == '__main__':
    tocar_nota_midi()