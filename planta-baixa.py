import pygame
import sys
import ctypes

# Inicialização do Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LINE_WIDTH = 1

largura = 700
altura = 500

# Função para desenhar o porão
def draw_basement(screen, width, height):
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    pygame.draw.rect(screen, BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do porão

# Função para desenhar o térreo
def draw_ground_floor(screen, width, height):
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    pygame.draw.rect(screen, BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno externo

# Função para desenhar o andar superior
def draw_upper_floor(screen, width, height):
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    pygame.draw.rect(screen, BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do andar superior

# Função para desenhar a planta baixa do andar selecionado
def draw_floor_plan(screen, floor):
    screen.fill(WHITE)  # Preenchendo o fundo com branco
    if floor == 'basement':
        draw_basement(screen, 600, 400)
    elif floor == 'ground':
        draw_ground_floor(screen, 700, 500)
    elif floor == 'upper':
        draw_upper_floor(screen, 600, 400)

# Configurando a janela
info = pygame.display.Info()
largura_tela, altura_tela = info.current_w, info.current_h
screen = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption("Planta Baixa da Casa - 2 Andares e Porão")

# Reposiciona a janela (no Windows)
x, y = 0, 0  # Posição desejada (x, y)
hwnd = pygame.display.get_wm_info()['window']
ctypes.windll.user32.SetWindowPos(hwnd, None, x, y, 0, 0, 0x0001)

# Variável para controlar o andar atual
current_floor = 'ground'
fullscreen = False

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                current_floor = 'basement'
            elif event.key == pygame.K_g:
                current_floor = 'ground'
            elif event.key == pygame.K_u:
                current_floor = 'upper'
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
                else:
                    screen = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    draw_floor_plan(screen, current_floor)
    pygame.display.flip()  # Atualizando a tela
