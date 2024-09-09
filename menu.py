import sys
import moveis

def menu(pygame):
    # Inicializa o Pygame
    pygame.init()

    # Define as cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)

    # Configura a janela
    largura, altura = 800, 600
    largura_casa, altura_casa = 0, 0
    menu = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Captura de Input")

    # Configura a fonte
    font = pygame.font.Font(None, 36)  # Fonte padrão com tamanho 36

    # Função para desenhar texto na tela
    def draw_text(text, font, color, surface, x, y):
        text_surface = font.render(text, True, color)  # Renderiza o texto
        text_rect = text_surface.get_rect(center=(x, y))  # Centraliza o texto
        surface.blit(text_surface, text_rect)  # Desenha o texto na superfície

    # Função para desenhar o prompt e o input na tela
    def draw_input_box(prompt, input_text, font, surface):
        # Desenha o prompt
        draw_text(prompt, font, BLACK, surface, largura // 2, altura // 2 - 50)
        
        # Desenha o input
        draw_text(input_text, font, BLUE, surface, largura // 2, altura // 2)

    # Variáveis de controle
    input_text = ''
    current_prompt = 'Digite a Largura:'
    prompt_index = 0
    prompts = ['Digite a Largura:', 'Digite a Altura:']
    input_mode = True  # Alterna entre prompts e input

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    if prompt_index == 0:
                        largura_casa = input_text
                    else:
                        altura_casa = input_text
                    # Muda para o próximo prompt quando ENTER é pressionado
                    if input_mode:
                        prompt_index += 1
                        if prompt_index < len(prompts):
                            current_prompt = prompts[prompt_index]
                            input_text = ''
                        else:
                            input_mode = False
                            with open('input_data.txt', 'w') as file:
                                file.write(f'{largura_casa} {altura_casa}')
                            pygame.quit()
                            moveis.get_escala()
                            return

                    else:
                        input_mode = True
                elif event.key == pygame.K_BACKSPACE:
                    # Remove o último caractere do texto
                    input_text = input_text[:-1]
                elif event.key == pygame.K_SPACE:
                    # Adiciona um espaço ao texto
                    input_text += ' '
                elif event.unicode.isdigit():
                    # Adiciona caracteres imprimíveis ao texto
                    input_text += event.unicode

        menu.fill(WHITE)  # Preenche o fundo com branco

        # Desenha o prompt e o texto de input
        draw_input_box(current_prompt, input_text, font, menu)

        pygame.display.flip()  # Atualiza a tela
