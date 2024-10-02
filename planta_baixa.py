import sys
import ctypes
import utils as ut
import moveis
import colors as cor

def planta(pygame, dados):
    # Inicialização do Pygame
    pygame.init()

    with open('input_data.txt', 'r') as file:
        data = file.readline().strip()
        parts = data.split(' ')
        largura_casa = int(parts[0])
        altura_casa = int(parts[1])

    # Configurando a janela
    info = pygame.display.Info()
    largura_tela, altura_tela = info.current_w, info.current_h

    largura_casa, altura_casa = ut.set_escala(largura_tela, altura_tela, largura_casa, altura_casa)
    escala = ut.get_escala(largura_casa, altura_casa)

    planta = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Térreo")

    # Reposiciona a janela (no Windows)
    x, y = 0, 0  # Posição desejada (x, y)
    janela = pygame.display.get_wm_info()['window']
    ctypes.windll.user32.SetWindowPos(janela, None, x, y, 0, 0, 0x0001)

    # Variável para controlar o andar atual
    current_floor = 'terreo'

    ROOMS = {}
    for andar in dados.andares:
        andar_nome = andar.nome
        ROOMS[andar_nome] = []
        
        for comodo in andar.comodos:
            # Atribuindo um ID único para cada cômodo
            comodo_id = f"{andar_nome}_{comodo.tipo}_{len(ROOMS[andar_nome]) + 1}"
            
            janela = None
            porta = None
            translationX, translationY = ut.coords(planta, largura_casa, altura_casa)

            # Criação da janela
            if comodo.janelax is not None and comodo.janelax != "":
                if (comodo.janelay == comodo.inicioy or comodo.janelay == comodo.inicioy + comodo.altura) and (comodo.iniciox <= comodo.janelax <= comodo.iniciox + comodo.largura):
                    janela = moveis.Janela(x=translationX + (comodo.janelax * escala), y=translationY + (comodo.janelay * escala), escala=escala, orientacao="H")
                elif (comodo.janelax == comodo.iniciox or comodo.janelax == comodo.iniciox + comodo.largura) and (comodo.inicioy <= comodo.janelay <= comodo.inicioy + comodo.altura):
                    janela = moveis.Janela(y=translationY + (comodo.janelay * escala), x=translationX + (comodo.janelax * escala), escala=escala, orientacao="V")

            # Criação da porta
            if comodo.portax is not None and comodo.portax != "":
                if (comodo.portay == comodo.inicioy or comodo.portay == comodo.inicioy + comodo.altura) and (comodo.iniciox <= comodo.portax <= comodo.iniciox + comodo.largura):
                    porta = moveis.Porta(x=translationX + (comodo.portax) * escala, y=translationY + (comodo.portay * escala), escala=escala, orientacao="H")
                elif (comodo.portax == comodo.iniciox or comodo.portax == comodo.iniciox + comodo.largura) and (comodo.inicioy <= comodo.portay <= comodo.inicioy + comodo.altura):
                    porta = moveis.Porta(y=translationY + (comodo.portay * escala), x=translationX + (comodo.portax) * escala, escala=escala, orientacao="V")

            tipo = comodo.tipo
            x, y, largura, altura = ut.converter_para_pixels_e_limitar(comodo.iniciox, comodo.inicioy, comodo.largura, comodo.altura, escala, largura_casa, altura_casa)
            
            # Adiciona o cômodo à estrutura
            if janela or porta:
                ROOMS[andar_nome].append([comodo_id, tipo, x + translationX, y + translationY, largura, altura, janela, porta])
            else:
                ROOMS[andar_nome].append([comodo_id, tipo, x + translationX, y + translationY, largura, altura])



    # for andar, comodos in ROOMS.items():
    #     print(f"#### {andar} ####")
    #     for comodo in comodos:
    #         print(comodo)
    MOVEIS = {
        "sala": [
            moveis.movel("Sofá de 2 lugares", 0.82, 1.72, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "sala", 1)),
            moveis.movel("Sofá de 3 lugares", 0.82, 2.10, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "sala", 1)),
            moveis.movel("Poltrona", 0.70, 0.80, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "sala", 1)),
            moveis.movel("Mesa de centro", 1.00, 0.60, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "sala", 1)),
            moveis.movel("Mesa auxiliar", 0.43, 0.40, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "sala", 1))
        ],
        "salaDeJantar": [
            moveis.movel("Mesa de 4 lugares", 0.90, 0.90, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "salaDeJantar", 1)),
            moveis.movel("Mesa de 6 lugares", 1.60, 0.90, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "salaDeJantar", 1)),
            moveis.movel("Aparador", 0.90, 0.36, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "salaDeJantar", 1)),
            moveis.movel("Cristaleira", 0.34, 0.84, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "salaDeJantar", 1))
        ],
        "quarto": [
            moveis.movel("Cama de casal", 1.44, 1.93, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "quarto", 1)),
            moveis.movel("Cama de solteiro", 0.94, 1.93, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "quarto", 1)),
            moveis.movel("Mesa auxiliar", 0.43, 0.40, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "quarto", 1)),
            moveis.movel("Guarda-roupa com duas portas", 0.40, 1.00, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "quarto", 1)),
            moveis.movel("Guarda-roupa com três portas", 0.40, 1.70, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "quarto", 1)),
            moveis.movel("Gaveteiro", 0.40, 0.87, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "quarto", 1))
        ],
        "cozinha": [
            moveis.movel("Fogão de 4 bocas", 0.58, 0.68, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "cozinha", 1)),
            moveis.movel("Fogão de 5 bocas", 0.77, 0.68, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "cozinha", 1)),
            moveis.movel("Geladeira com 1 porta", 0.62, 0.75, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "cozinha", 1)),
            moveis.movel("Geladeira com 2 portas", 0.83, 0.79, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "cozinha", 1)),
            moveis.movel("Armário", 0.34, 1.68, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "cozinha", 1)),
            moveis.movel("Pia", 1.00, 0.50, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "cozinha", 1))
        ],
        "banheiro": [
            moveis.movel("Vaso sanitário", 0.37, 0.64, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "banheiro", 1)),
            moveis.movel("Banheira", 0.71, 1.65, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "banheiro", 1)),
            moveis.movel("Pia com armário", 0.70, 0.45, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "banheiro", 1)),
            # moveis.movel("Box de banheiro", 1.50, 2.00, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "banheiro", 1))
        ],
        "areaServico": [
            moveis.movel("Máquina de lavar roupa", 0.60, 0.65, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "areaServico", 1)),
            moveis.movel("Secadora", 0.60, 0.65, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "areaServico", 1)),
            moveis.movel("Tanque de lavar", 0.55, 0.50, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "areaServico", 1)),
            moveis.movel("Cesto de roupa suja", 0.50, 0.40, cor.BEIGE, escala, ut.encontrar_comodo(ROOMS, "areaServico", 1))
        ],
        "ginastica": [
            moveis.movel("Esteira", 1.50, 0.70, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "ginastica", 1)),
            moveis.movel("Bicicleta ergométrica", 1.20, 0.50, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "ginastica", 1)),
            moveis.movel("Banco de supino", 1.80, 0.60, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "ginastica", 1)),
            moveis.movel("Halteres", 0.50, 0.30, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "ginastica", 1))
        ]
    }
    # Seleciona móveis para a sala de estar (sala)
    MOVEIS_ESCOLHIDOS = ut.escolher_todos_moveis(ROOMS, MOVEIS, escala)
    # print(MOVEIS_ESCOLHIDOS[0])

    ####ESCOLHER AQUI PARA COMODO EM MOVEIS#####

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    current_floor = 'laje'
                    pygame.display.set_caption("Porão")

                elif event.key == pygame.K_g:
                    current_floor = 'terreo'
                    pygame.display.set_caption("Térreo")
                    
                elif event.key == pygame.K_u:
                    current_floor = 'pAndar'
                    pygame.display.set_caption("Primeiro Andar")

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                            
        ut.draw_floor_plan(planta, current_floor, largura_casa, altura_casa, ROOMS, MOVEIS_ESCOLHIDOS)
        pygame.display.flip()  # Atualizando a tela