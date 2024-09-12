import pygame
import moveis as mv
import colors as cor
import random

AREA_MAX_PIXEL = 1920 * 1080
PIXEL_METRO = 110
LINE_WIDTH = 1

# Função para desenhar o porão
def draw_basement(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do porão

# Função para desenhar o térreo
def draw_ground_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno externo

# Função para desenhar o andar superior
def draw_upper_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do andar superior

def draw_rooms(screen, rooms, moveis):
    for room in rooms:
        comodo, x, y, width, height = room
        pygame.draw.rect(screen, cor.GREEN, (x, y, width, height), LINE_WIDTH)

        mv.draw_furnitures(screen, comodo, moveis)

# Função para desenhar a planta baixa do andar selecionado
def draw_floor_plan(screen, floor, largura_casa, altura_casa, ROOMS, MOVEIS):
    screen.fill(cor.WHITE)

    if floor == 'basement':
        draw_basement(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[0], MOVEIS)
    elif floor == 'ground':
        draw_ground_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[1], MOVEIS)
    elif floor == 'upper':
        draw_upper_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS[2], MOVEIS)

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

def encontrar_comodo(rooms, comodo_nome):
    for floor in rooms:
        for room in floor:
            if room[0] == comodo_nome:
                return room[1:]  # Retorna x, y, largura, altura
    return None

def escolher_moveis(moveis, rooms, comodo, escala):
    if comodo in moveis:
        moveis_selecionados = []
        medidas = encontrar_comodo(rooms, comodo)
        
        # Seleciona 3 móveis aleatoriamente do cômodo
        for movel in random.sample(moveis[comodo], 3):
            posicao_valida_flag = False
            
            while not posicao_valida_flag:
                # Cria uma nova instância do móvel com posição aleatória
                novo_movel = mv.movel(movel.nome, movel.largura/escala, movel.altura/escala, movel.cor, escala, medidas)
                posicao_valida_flag = posicao_valida(novo_movel, moveis_selecionados, medidas)
            
            moveis_selecionados.append(novo_movel)
        
        return moveis_selecionados
    return []

def escolher_todos_moveis(rooms, moveis, escala):
    moveis_escolhidos = {}
    
    # Percorre cada cômodo e seleciona 3 móveis aleatoriamente
    for floor in rooms:
        for room in floor:
            comodo = room[0]  # Nome do cômodo
            moveis_do_comodo = escolher_moveis(moveis, rooms, comodo, escala)  # Seleciona 3 móveis
            if moveis_do_comodo:
                moveis_escolhidos[comodo] = moveis_do_comodo  # Associa os móveis ao cômodo

    return moveis_escolhidos

def posicao_valida(movel, moveis_existentes, medidas):
    # return True
    # Verifica se o móvel está dentro dos limites do cômodo
    if movel.x < medidas[0] or movel.y < medidas[1] or \
       movel.x + movel.largura > medidas[0] + medidas[2] or \
       movel.y + movel.altura > medidas[1] + medidas[3]:
        return False

    # Verifica sobreposição com outros móveis
    for outro_movel in moveis_existentes:
        if (movel.x < outro_movel.x + outro_movel.largura and
            movel.x + movel.largura > outro_movel.x and
            movel.y < outro_movel.y + outro_movel.altura and
            movel.y + movel.altura > outro_movel.y):
            return False
    
    return True