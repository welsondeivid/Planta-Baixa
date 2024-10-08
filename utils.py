import pygame
import moveis as mv
import colors as cor
import random

AREA_MAX_PIXEL = 1920 * 1080
PIXEL_METRO = 50
LINE_WIDTH = 1

comodos_cores = {
    'sala': cor.YELLOW,
    'cozinha': cor.ORANGE,
    'banheiro': cor.AQUA,
    'corredor': cor.GRAY,
    'escada': cor.SANDY_BROWN,
    'salaDeJantar': cor.TOMATO,
    'areaServico': cor.SILVER,
    'closet': cor.PURPLE,
    'quarto': cor.OLIVE,
    'ginastica': cor.GOLD,
}

# Adicione esta variável global no início do arquivo
frame_counter = 0

# Função para desenhar o porão
def draw_laje(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do porão

# Função para desenhar o Térreo
def draw_terreo_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno externo

# Função para desenhar o andar superior
def draw_pAndar_floor(screen, width, height):
    x, y = coords(screen, width, height)
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH)  # Contorno do andar superior

import pygame

# Adicione esta variável global no início do arquivo
frame_counter = 0

def draw_rooms(screen, rooms, moveis, andar):
    global frame_counter

    # Configuração da fonte
    font = pygame.font.Font(None, 36)  # Você pode ajustar o tamanho da fonte conforme necessário
    
    for room in rooms:

        janela = None
        porta = None

        id, comodo, x, y, width, height, *rest = room
        
        
        if len(rest) == 1:
            if isinstance(rest[0], mv.Janela):
                janela = rest[0]
            elif isinstance(rest[0], mv.Porta):
                porta = rest[0]
        elif len(rest) == 2:
            if isinstance(rest[0], mv.Janela):
                janela = rest[0]
            elif isinstance(rest[0], mv.Porta):
                porta = rest[0]
            if isinstance(rest[1], mv.Janela):
                janela = rest[1]
            elif isinstance(rest[1], mv.Porta):
                porta = rest[1]
        
        pygame.draw.rect(screen, comodos_cores[comodo], (x, y, width, height))
        
        if porta:
            if porta.largura:
                porta.drawH(screen)
            elif porta.altura:
                porta.drawV(screen)

        if janela:
            if janela.largura:
                janela.drawH(screen)
            elif janela.altura:
                janela.drawV(screen)

        frame_counter += 1
        
        # Desenha os móveis do cômodo atual
        mv.draw_furnitures(screen, comodo, andar, moveis)

        texto = comodo[:2].upper()  # Pega as duas primeiras letras do nome do cômodo
        if comodo == "salaDeJantar":
            texto = "SJ"
        elif comodo == "areaServico":
            texto = "AS"
        texto_surface = font.render(texto, True, (0, 0, 0))  # Renderiza o texto em preto
        texto_rect = texto_surface.get_rect()
        texto_rect.center = (x + width // 2, y + height // 2)  # Posiciona o texto no centro do cômodo
        screen.blit(texto_surface, texto_rect)

def draw_corridors(screen, corridors, andar):
    for corridor in corridors:
        x, y, width, height = corridor
        pygame.draw.rect(screen, comodos_cores["corredor"], (x, y, width, height))

def draw_limites(screen, limites):
    x, y, width, height = limites
    pygame.draw.rect(screen, cor.BLACK, (x, y, width, height), LINE_WIDTH+5)

def draw_porta_frontal(screen, portaFrontal):
    if portaFrontal:
        if portaFrontal.largura:
            portaFrontal.drawH(screen)
        elif portaFrontal.altura:
            portaFrontal.drawV(screen)

# Função para desenhar a planta baixa do andar selecionado
def draw_floor_plan(screen, floor, largura_casa, altura_casa, ROOMS, CORRIDORS, MOVEIS_ESCOLHIDOS, LIMITES, portaFrontal):
    screen.fill(cor.WHITE)

    if floor == 'laje':
        # draw_laje(screen, largura_casa, altura_casa)
        draw_limites(screen, LIMITES["Laje"])
        draw_corridors(screen, CORRIDORS["Laje"], "Laje")
        draw_rooms(screen, ROOMS["Laje"], MOVEIS_ESCOLHIDOS, "Laje")
        desenhar_legenda(screen, MOVEIS_ESCOLHIDOS, LIMITES["Laje"], "Laje")
    elif floor == 'terreo':
        # draw_terreo_floor(screen, largura_casa, altura_casa)
        draw_limites(screen, LIMITES["Térreo"])
        draw_corridors(screen, CORRIDORS["Térreo"], "Térreo")
        draw_rooms(screen, ROOMS["Térreo"], MOVEIS_ESCOLHIDOS,"Térreo")
        draw_porta_frontal(screen, portaFrontal)
        desenhar_legenda(screen, MOVEIS_ESCOLHIDOS, LIMITES["Térreo"], "Térreo")
    elif floor == 'pAndar':
        # draw_pAndar_floor(screen, largura_casa, altura_casa)
        draw_limites(screen, LIMITES["1 Andar"])
        draw_corridors(screen, CORRIDORS["1 Andar"], "1 Andar")
        draw_rooms(screen, ROOMS["1 Andar"], MOVEIS_ESCOLHIDOS, "1 Andar")
        desenhar_legenda(screen, MOVEIS_ESCOLHIDOS, LIMITES["1 Andar"], "1 Andar")

def coords(screen, width, height):
    x = round((screen.get_width() - width) // 2)
    y = round((screen.get_height() - height) // 2)
    return x, y

def get_escala(largura_casa, altura_casa):
    escala = (largura_casa * altura_casa) / AREA_MAX_PIXEL
    escala_pixel = round(PIXEL_METRO * escala)
    return escala_pixel

def set_escala(largura_tela, altura_tela, largura_casa, altura_casa):
    escala = min(largura_tela / largura_casa, altura_tela / altura_casa)

    return escala * largura_casa, escala * altura_casa

def fillCorners(corridors):
    tam = len(corridors)
    for i in range(tam):
        for j in range(i+1, tam):
            if abs(corridors[i][0] - corridors[j][0]) == 1 and abs(corridors[i][1] - corridors[j][1]) == 1:
                # Adiciona as coordenadas dos pontos dos cantos entre os corredores
                corridors.append([corridors[i][0], corridors[j][1]])
                corridors.append([corridors[j][0], corridors[i][1]])
def encontrar_comodo(rooms, comodo_nome):
    for floor_name, floor_rooms in rooms.items():  # Itera sobre os andares e seus cômodos
        for room in floor_rooms:
            comodo = room[0].split('_')[1]  # Obtém o nome do cômodo
            if comodo == comodo_nome:
                return room[2:]  # Retorna x, y, largura, altura
    return None  # Retorna None se o cômodo não for encontrado

def pegar_medidas_por_id(dicionario, id_procurado):
    # Percorre cada chave (andar) e suas respectivas listas de cômodos
    for andar, comodos in dicionario.items():
        # Percorre a lista de cômodos em cada andar
        for comodo in comodos:
            if comodo[0] == id_procurado:  # Compara o ID
                # Retorna as medidas (posição x, posição y, largura, altura)
                return comodo[2:6]  # Índices 2, 3, 4, 5 correspondem a x, y, largura, altura
    return None  # Retorna None se o ID não for encontrado

def escolher_moveis(moveis, rooms, comodo_id, escala):
    andar, tipo_comodo, index = comodo_id.split('_')  # Corrigido para desempacotar corretamente

    if tipo_comodo in moveis:
        moveis_selecionados = []
        medidas = pegar_medidas_por_id(rooms, comodo_id)  # Preenche medidas com as dimensões do cômodo
        if not medidas:
            return []  # Retorna vazio se não encontrar as medidas do cômodo
        
        # Seleciona 3 móveis aleatoriamente do cômodo
        for movel in random.sample(moveis[tipo_comodo], 3):
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
            # print(novo_movel)
            moveis_selecionados.append(novo_movel)
        
        return moveis_selecionados
    return []


def escolher_todos_moveis(rooms, moveis, escala):
    moveis_escolhidos = {}
    
    # Percorre cada andar no dicionário de andares
    for andar, lista_de_comodos in rooms.items():
        # Percorre cada cômodo na lista do andar
        for room in lista_de_comodos:
            comodo = room[0]  # Desestrutura o cômodo
            
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

def converter_para_pixels_e_limitar(x, y, largura, altura, escala, largura_planta, altura_planta):
    """
    Converte coordenadas baseadas em unidades para pixels e ajusta para que fiquem dentro dos limites da planta.
    """
    x_pixel = x * escala
    y_pixel = y * escala
    largura_pixel = largura * escala
    altura_pixel = altura * escala
        
    # Ajustar x e largura
    if x_pixel < 0:
        x_pixel = 0
    if x_pixel + largura_pixel > largura_planta:
        largura_pixel = largura_planta - x_pixel
    
    # Ajustar y e altura
    if y_pixel < 0:
        y_pixel = 0
    if y_pixel + altura_pixel > altura_planta:
        altura_pixel = altura_planta - y_pixel

    return x_pixel, y_pixel, largura_pixel, altura_pixel

def desenhar_legenda(planta, moveis_escolhidos, limites, andar_atual):
    # Definir posição inicial da legenda
    x_legenda = limites[2] + 200  # À direita do andar
    y_legenda = limites[1]  # Alinhado com o topo do andar
    
    # Definir tamanho do retângulo de cor e espaçamento
    tamanho_rect = 15
    espaco = 5
    
    # Definir fonte
    fonte = pygame.font.SysFont('Arial', 14)
    
    # Calcular o tamanho da legenda
    largura_legenda = 200
    altura_legenda = limites[3] - limites[1]
    
    # Desenhar o fundo da legenda
    cor_fundo = cor.LIGHT_GRAY  # Definir uma cor de fundo clara
    pygame.draw.rect(planta, cor_fundo, (x_legenda, y_legenda, largura_legenda, altura_legenda))
    
    # Adicionar uma borda à legenda
    pygame.draw.rect(planta, cor.BLACK, (x_legenda, y_legenda, largura_legenda, altura_legenda), 1)
    
    # Título da legenda
    titulo = fonte.render("Legenda de Móveis", True, (0, 0, 0))
    planta.blit(titulo, (x_legenda + 5, y_legenda + 5))
    y_legenda += 25
    
    # Iterar sobre os móveis escolhidos do andar atual
    for comodo_id, moveis in moveis_escolhidos.items():
        if comodo_id.startswith(andar_atual):
            for movel in moveis:
                # Desenhar retângulo com a cor do móvel
                pygame.draw.rect(planta, movel.cor, (x_legenda + 5, y_legenda, tamanho_rect, tamanho_rect))
                
                # Escrever o nome do móvel
                texto = fonte.render(movel.nome, True, (0, 0, 0))
                planta.blit(texto, (x_legenda + tamanho_rect + espaco + 5, y_legenda))
                
                y_legenda += tamanho_rect + espaco
            
            # Adicionar espaço extra entre cômodos
            y_legenda += 10
        
        # Verificar se a legenda ultrapassou o limite inferior do andar
        if y_legenda > limites[3] - 20:
            # Mover para uma nova coluna à direita
            x_legenda += largura_legenda
            y_legenda = limites[1]
            
            # Desenhar novo fundo para a nova coluna
            pygame.draw.rect(planta, cor_fundo, (x_legenda, limites[1], largura_legenda, altura_legenda))
            pygame.draw.rect(planta, cor.BLACK, (x_legenda, limites[1], largura_legenda, altura_legenda), 1)