import pygame
import moveis

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

AREA_MAX_PIXEL = 1920 * 1080
PIXEL_METRO = 110
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

def draw_rooms(screen, rooms, largura_casa, altura_casa):
    for room in rooms:
        comodo, x, y, width, height = room
        pygame.draw.rect(screen, GREEN, (x, y, width, height), LINE_WIDTH)

        moveis.draw_furnitures(screen, comodo, x, y, width, height, largura_casa, altura_casa)

# Função para desenhar a planta baixa do andar selecionado
def draw_floor_plan(screen, floor, largura_casa, altura_casa):
    screen.fill(WHITE)

    escala = get_escala(largura_casa, altura_casa)

    ROOMS = [
        [["bedroom", 100, 300, 4*escala, 3*escala], ["bath", 500, 800, 1.5*escala, 2*escala]],
        [["livingroom", 500, 300, 5*escala, 6*escala]],
        [["playroom", 100, 300, 6*escala, 5*escala], ["socialbath", 100, 400, 2*escala, 4*escala]]
    ]

    if floor == 'basement':
        draw_basement(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[0], largura_casa, altura_casa)
    elif floor == 'ground':
        draw_ground_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[1], largura_casa, altura_casa)
    elif floor == 'upper':
        draw_upper_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[2], largura_casa, altura_casa)

def coords(screen, width, height):
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    return x, y

def get_escala(largura_casa, altura_casa):

    escala = (largura_casa * altura_casa) / AREA_MAX_PIXEL
    escala_pixel = round(PIXEL_METRO * escala)
    return escala_pixel

def set_escala(largura_tela, altura_tela, largura_casa, altura_casa):
    escala = min(largura_tela / largura_casa, altura_tela / altura_casa)

    return escala * largura_casa, escala * altura_casa
