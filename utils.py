import pygame
import moveis as mv
import colors as cor
import random

AREA_MAX_PIXEL = 1920 * 1080
PIXEL_METRO = 110
LINE_WIDTH = 1

# Função para desenhar o porão
def draw_laje(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do porão

# Função para desenhar o térreo
def draw_terreo_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno externo

# Função para desenhar o andar superior
def draw_pAndar_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do andar superior

def draw_rooms(screen, rooms, moveis):
    for room in rooms:  # Itera sobre cada andar
        comodo, x, y, width, height = room
        pygame.draw.rect(screen, cor.GREEN, (x, y, width, height), LINE_WIDTH)

        # Desenha os móveis do cômodo atual
        mv.draw_furnitures(screen, comodo, moveis)


# Função para desenhar a planta baixa do andar selecionado
def draw_floor_plan(screen, floor, largura_casa, altura_casa, ROOMS, MOVEIS):
    screen.fill(cor.WHITE)

    if floor == 'laje':
        draw_laje(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS["Laje"], MOVEIS)
    elif floor == 'terreo':
        draw_terreo_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS["Terreo"], MOVEIS)
    elif floor == 'pAndar':
        draw_pAndar_floor(screen, largura_casa, altura_casa)
        draw_rooms(screen, ROOMS["1 Andar"], MOVEIS)

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
    for floor_name, floor_rooms in rooms.items():  # Itera sobre os andares e seus cômodos
        # print(f"Verificando andar: {floor_name}")
        for room in floor_rooms:
            # print("Verificando cômodo:", room[0])
            if room[0] == comodo_nome:
                # print("Cômodo encontrado:", comodo_nome, room[1:])
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
                
                # Verifica se a posição é válida
                if not posicao_valida(novo_movel, moveis_selecionados, medidas):
                    # Tenta rotacionar o móvel (troca largura e altura)
                    novo_movel = mv.movel(movel.nome, movel.altura/escala, movel.largura/escala, movel.cor, escala, medidas)
                
                # Se ainda não couber, tenta uma nova posição aleatória
                if not posicao_valida(novo_movel, moveis_selecionados, medidas):
                    novo_movel = mv.movel(movel.nome, movel.largura/escala, movel.altura/escala, movel.cor, escala, medidas)
                
                # Verifica se a nova posição/rotação é válida
                posicao_valida_flag = posicao_valida(novo_movel, moveis_selecionados, medidas)
            
            moveis_selecionados.append(novo_movel)
        
        return moveis_selecionados
    return []

def escolher_todos_moveis(rooms, moveis, escala):
    moveis_escolhidos = {}
    
    # Percorre cada andar no dicionário de andares
    for andar, lista_de_comodos in rooms.items():
        # Percorre cada cômodo na lista do andar
        for room in lista_de_comodos:
            comodo, x, y, width, height = room  # Desestrutura o cômodo
            
            # Seleciona móveis para o cômodo
            moveis_do_comodo = escolher_moveis(moveis, rooms, comodo, escala)
            
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