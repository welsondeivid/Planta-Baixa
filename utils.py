import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

LINE_WIDTH = 1

tiles = {}

tile_width = 50
tile_height = 50

def create_tiles(largura_casa, altura_casa, current_floor):
    global tiles  # Certifique-se de atualizar o dicionário global
    tile_size = 50
    tiles = {}  # Limpa o dicionário existente
    n = largura_casa // tile_size
    m = altura_casa // tile_size

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = (i - 1) * tile_size
            y = (j - 1) * tile_size
            tile_name = f"{current_floor}_tile_{i}_{j}"
            tiles[tile_name] = {'andar': current_floor, 'x': x, 'y': y, 'ocupado': False}

def colorir_tile(tile_name, color, screen):
    if tile_name in tiles:
        tile = tiles[tile_name]
        x, y = tile['x'], tile['y']
        pygame.draw.rect(screen, color, (x, y, tile_width, tile_height))

def draw_grid(screen, width, height):
    start_x, start_y = coords(screen, width, height)
    for x in range(start_x, start_x + width, tile_width):
        pygame.draw.line(screen, BLACK, (x, start_y), (x, start_y + height))
    for y in range(start_y, start_y + height, tile_height):
        pygame.draw.line(screen, BLACK, (start_x, y), (start_x + width, y))

def coords(screen, width, height):
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    return x, y
