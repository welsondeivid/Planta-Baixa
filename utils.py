import pygame
import moveis

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

LINE_WIDTH = 1

# Função para desenhar o porão
def draw_basement(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do porão

# Função para desenhar o térreo
def draw_ground_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno externo

# Função para desenhar o andar superior
def draw_upper_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do andar superior

def draw_rooms(screen, rooms):
    for room in rooms:
        comodo, x, y, width, height = room
        pygame.draw.rect(screen, GREEN, (x, y, width, height), LINE_WIDTH)

        moveis.draw_furnitures(screen, comodo, x, y, width, height)

# Função para desenhar a planta baixa do andar selecionado
def draw_floor_plan(screen, floor, largura_casa, altura_casa):
    screen.fill(WHITE)

    escala = moveis.get_escala()

    ROOMS = [
        [["bedroom", 100*escala, 300*escala, 50*escala, 50*escala], ["bath", 500*escala, 800*escala, 200*escala, 120*escala]],
        [["dinnerroom,", 200*escala, 300*escala, 700*escala, 300*escala], ["livingroom", 500*escala, 800*escala, 200*escala, 120*escala]],
        [["playroom", 100*escala, 300*escala, 300*escala, 120*escala], ["socialbath", 100*escala, 400*escala, 250*escala, 200*escala]]
    ]

    if floor == 'basement':
        draw_basement(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[0])
    elif floor == 'ground':
        draw_ground_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[1])
    elif floor == 'upper':
        draw_upper_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[2])

def coords(screen, width, height):
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    return x, y
