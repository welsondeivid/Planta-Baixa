import sys
import ctypes
import utils as ut

def planta(pygame):
    # Inicialização do Pygame
    pygame.init()

    with open('input_data.txt', 'r') as file:
        data = file.readline().strip()
        largura_casa, altura_casa = map(int, data.split(' '))

    # Configurando a janela
    info = pygame.display.Info()
    largura_tela, altura_tela = info.current_w, info.current_h
    planta = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Térreo")

    # Reposiciona a janela (no Windows)
    x, y = 0, 0  # Posição desejada (x, y)
    janela = pygame.display.get_wm_info()['window']
    ctypes.windll.user32.SetWindowPos(janela, None, x, y, 0, 0, 0x0001)

    # Variável para controlar o andar atual
    current_floor = 'ground'
    # fullscreen = False

    ######GERAR OS MOVEIS AQUI#############

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    current_floor = 'basement'
                    pygame.display.set_caption("Porão")
                    # print(ut.tiles)

                elif event.key == pygame.K_g:
                    current_floor = 'ground'
                    pygame.display.set_caption("Térreo")
                    # print(ut.tiles)
                    
                elif event.key == pygame.K_u:
                    current_floor = 'upper'
                    pygame.display.set_caption("Primeiro Andar")
                    # print(ut.tiles)

                # elif event.key == pygame.K_p:
                #     coord = coords(planta, largura_casa, altura_casa)
                #     x = random.randint(coord[0], largura_casa - coord[0])
                #     y = random.randint(coord[1], altura_casa - coord[1])
                # if event.key == pygame.K_f:
                #     fullscreen = not fullscreen
                #     if fullscreen:
                #         planta = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
                #     else:
                #         planta = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                            
        ut.draw_floor_plan(planta, current_floor, largura_casa, altura_casa)
        pygame.display.flip()  # Atualizando a tela
