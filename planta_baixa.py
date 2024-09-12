import sys
import ctypes
import utils as ut
import moveis
import colors as cor

def planta(pygame):
    # Inicialização do Pygame
    pygame.init()

    with open('input_data.txt', 'r') as file:
        data = file.readline().strip()
        largura_casa, altura_casa = map(int, data.split(' '))

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
    current_floor = 'ground'

    ######GERAR OS MOVEIS AQUI#############
    ROOMS = [
        [["bedroom", 100, 300, 4 * escala, 3 * escala], ["bathroom", 500, 800, 2 * escala, 2 * escala]],
        [["livingroom", 500, 300, 5 * escala, 6 * escala], ["kitchen", 900, 800, 4 * escala, 3 * escala], ["diningroom", 100, 100, 4 * escala, 4 * escala]],
        [["playroom", 100, 300, 6 * escala, 5 * escala], ["socialbath", 800, 300, 2 * escala, 4 * escala]]
    ]
    
    MOVEIS = {
    "livingroom": [
        moveis.movel("Sofá de 2 lugares", 0.82, 1.72, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "livingroom")),
        moveis.movel("Sofá de 3 lugares", 0.82, 2.10, cor.SANDY_BROWN, escala, ut.encontrar_comodo(ROOMS, "livingroom")),
        moveis.movel("Poltrona", 0.70, 0.80, cor.DARK_BLUE, escala, ut.encontrar_comodo(ROOMS, "livingroom")),
        moveis.movel("Mesa de centro", 1.00, 0.60, cor.BLACK, escala, ut.encontrar_comodo(ROOMS, "livingroom")),
        moveis.movel("Mesa auxiliar", 0.43, 0.40, cor.DARK_GRAY, escala, ut.encontrar_comodo(ROOMS, "livingroom"))
    ],
    "diningroom": [
        moveis.movel("Mesa de 4 lugares", 0.90, 0.90, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "diningroom")),
        moveis.movel("Mesa de 6 lugares", 1.60, 0.90, cor.SANDY_BROWN, escala, ut.encontrar_comodo(ROOMS, "diningroom")),
        moveis.movel("Aparador", 0.90, 0.36, cor.DARK_BLUE, escala, ut.encontrar_comodo(ROOMS, "diningroom")),
        moveis.movel("Cristaleira", 0.34, 0.84, cor.BLACK, escala, ut.encontrar_comodo(ROOMS, "diningroom"))
    ],
    "bedroom": [
        moveis.movel("Cama de casal", 1.44, 1.93, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "bedroom")),
        moveis.movel("Cama de solteiro", 0.94, 1.93, cor.SANDY_BROWN, escala, ut.encontrar_comodo(ROOMS, "bedroom")),
        moveis.movel("Mesa auxiliar", 0.43, 0.40, cor.DARK_BLUE, escala, ut.encontrar_comodo(ROOMS, "bedroom")),
        moveis.movel("Guarda-roupa com duas portas", 0.40, 1.00, cor.BLACK, escala, ut.encontrar_comodo(ROOMS, "bedroom")),
        moveis.movel("Guarda-roupa com três portas", 0.40, 1.70, cor.DARK_GRAY, escala, ut.encontrar_comodo(ROOMS, "bedroom")),
        moveis.movel("Gaveteiro", 0.40, 0.87, cor.LIGHT_GRAY, escala, ut.encontrar_comodo(ROOMS, "bedroom"))
    ],
    "kitchen": [
        moveis.movel("Fogão de 4 bocas", 0.58, 0.68, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "kitchen")),
        moveis.movel("Fogão de 5 bocas", 0.77, 0.68, cor.SANDY_BROWN, escala, ut.encontrar_comodo(ROOMS, "kitchen")),
        moveis.movel("Geladeira com 1 porta", 0.62, 0.75, cor.DARK_BLUE, escala, ut.encontrar_comodo(ROOMS, "kitchen")),
        moveis.movel("Geladeira com 2 portas", 0.83, 0.79, cor.BLACK, escala, ut.encontrar_comodo(ROOMS, "kitchen")),
        moveis.movel("Armário", 0.34, 1.68, cor.DARK_GRAY, escala, ut.encontrar_comodo(ROOMS, "kitchen")),
        moveis.movel("Pia", 1.00, 0.50, cor.LIGHT_GRAY, escala, ut.encontrar_comodo(ROOMS, "kitchen"))
    ],
    "bathroom": [
        moveis.movel("Vaso sanitário", 0.37, 0.64, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "bathroom")),
        moveis.movel("Banheira", 0.71, 1.65, cor.SANDY_BROWN, escala, ut.encontrar_comodo(ROOMS, "bathroom")),
        moveis.movel("Pia com armário", 0.70, 0.45, cor.DARK_BLUE, escala, ut.encontrar_comodo(ROOMS, "bathroom")),
        moveis.movel("Box de banheiro", 1.50, 2.00, cor.BLACK, escala, ut.encontrar_comodo(ROOMS, "bathroom"))
    ],
    "socialbath": [
        moveis.movel("Vaso sanitário", 0.37, 0.64, cor.BROWN, escala, ut.encontrar_comodo(ROOMS, "bathroom")),
        moveis.movel("Banheira", 0.71, 1.65, cor.SANDY_BROWN, escala, ut.encontrar_comodo(ROOMS, "bathroom")),
        moveis.movel("Pia com armário", 0.70, 0.45, cor.DARK_BLUE, escala, ut.encontrar_comodo(ROOMS, "bathroom")),
        moveis.movel("Box de banheiro", 1.50, 2.00, cor.BLACK, escala, ut.encontrar_comodo(ROOMS, "bathroom"))
    ]
}
    # Seleciona móveis para a sala de estar (livingroom)
    MOVEIS_ESCOLHIDOS = ut.escolher_todos_moveis(ROOMS, MOVEIS, escala)
    print(MOVEIS_ESCOLHIDOS)

    ####ESCOLHER AQUI PARA COMODO EM MOVEIS#####

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

                elif event.key == pygame.K_g:
                    current_floor = 'ground'
                    pygame.display.set_caption("Térreo")
                    
                elif event.key == pygame.K_u:
                    current_floor = 'upper'
                    pygame.display.set_caption("Primeiro Andar")

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                            
        ut.draw_floor_plan(planta, current_floor, largura_casa, altura_casa, ROOMS, MOVEIS_ESCOLHIDOS)
        pygame.display.flip()  # Atualizando a tela