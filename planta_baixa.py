import sys
import pygame
import ctypes
import utils as ut
import random

def planta():
    # Inicialização do Pygame
    pygame.init()

    with open('input_data.txt', 'r') as file:
        data = file.readline().strip()
        largura_casa, altura_casa = map(int, data.split(' '))

    # Definindo as cores
    
    # Função para desenhar o porão
    def draw_basement(screen, width, height):
        x, y = ut.coords(screen, width, height)
        pygame.draw.rect(screen, ut.BLACK, (x, y, width, height), ut.LINE_WIDTH)  # Contorno do porão
        ut.draw_grid(screen, width, height)

    # Função para desenhar o térreo
    def draw_ground_floor(screen, width, height):
        x, y = ut.coords(screen, width, height)
        pygame.draw.rect(screen, ut.BLACK, (x, y, width, height), ut.LINE_WIDTH)  # Contorno externo
        ut.draw_grid(screen, width, height)

    # Função para desenhar o andar superior
    def draw_upper_floor(screen, width, height):
        x, y = ut.coords(screen, width, height)
        pygame.draw.rect(screen, ut.BLACK, (x, y, width, height), ut.LINE_WIDTH)  # Contorno do andar superior
        ut.draw_grid(screen, width, height)

    # Função para desenhar a planta baixa do andar selecionado
    def draw_floor_plan(screen, floor, x, y):
        screen.fill(ut.WHITE)  # Preenchendo o fundo com branco
        
        # text = f"X: {x}, Y: {y}"
        # text_surface = font.render(text, True, ut.BLACK)
        # text_rect = text_surface.get_rect(topright=(planta.get_width() - 10, 10))
        # planta.blit(text_surface, text_rect)

        if floor == 'basement':
            draw_basement(screen, largura_casa, altura_casa)
        elif floor == 'ground':
            draw_ground_floor(screen, largura_casa, altura_casa)
        elif floor == 'upper':
            draw_upper_floor(screen, largura_casa, altura_casa)

        # pygame.draw.rect(planta, GREEN, (x, y, largura_casa - x, altura_casa - y), ut.LINE_WIDTH)

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

    # font = pygame.font.Font(None, 36)
    # coord = coords(planta, largura_casa, altura_casa)
    # print(altura_casa)
    # x = random.randint(coord[0], largura_casa - coord[0])
    # y = random.randint(coord[1], altura_casa - coord[1])

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
                    ut.create_tiles(largura_casa, altura_casa, current_floor)
                    xt = random.randint(0, largura_casa // 50)
                    yt = random.randint(0, largura_casa // 50)
                    ut.colorir_tile(ut.tiles, f"{current_floor}tiles_{xt}_{yt}", ut.GREEN, planta)
                    # print(ut.tiles)

                elif event.key == pygame.K_g:
                    current_floor = 'ground'
                    pygame.display.set_caption("Térreo")
                    ut.create_tiles(largura_casa, altura_casa, current_floor)
                    xt = random.randint(0, largura_casa // 50)
                    yt = random.randint(0, largura_casa // 50)
                    ut.colorir_tile(ut.tiles, f"{current_floor}tiles_{xt}_{yt}", ut.GREEN, planta)
                    # print(ut.tiles)
                    
                elif event.key == pygame.K_u:
                    current_floor = 'upper'
                    pygame.display.set_caption("Primeiro Andar")
                    ut.create_tiles(largura_casa, altura_casa, current_floor)
                    xt = random.randint(0, largura_casa // 50)
                    yt = random.randint(0, largura_casa // 50)
                    ut.colorir_tile(ut.tiles, f"{current_floor}tiles_{xt}_{yt}", ut.GREEN, planta)
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
                            
        draw_floor_plan(planta, current_floor, x, y)
        pygame.display.flip()  # Atualizando a tela
