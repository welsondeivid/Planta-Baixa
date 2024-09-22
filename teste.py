import pygame

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
        largura_pixel += x_pixel
        x_pixel = 0
    if x_pixel + largura_pixel > largura_planta:
        largura_pixel = largura_planta - x_pixel
    
    # Ajustar y e altura
    if y_pixel < 0:
        altura_pixel += y_pixel
        y_pixel = 0
    if y_pixel + altura_pixel > altura_planta:
        altura_pixel = altura_planta - y_pixel
    
    return x_pixel, y_pixel, largura_pixel, altura_pixel

# Configuração do Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 240))
clock = pygame.time.Clock()

# Dados do cômodo
x_unidade, y_unidade, largura_unidade, altura_unidade = 0, 0, 10, 4
escala = 10  # Escala em pixels por unidade

# Limites da planta
largura_planta = 1920
altura_planta = 240

# Converter e ajustar coordenadas
x_pixel, y_pixel, largura_pixel, altura_pixel = converter_para_pixels_e_limitar(
    x_unidade, y_unidade, largura_unidade, altura_unidade, escala, largura_planta, altura_planta
)

# Renderizar no Pygame
screen.fill((255, 255, 255))  # Cor de fundo branca
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x_pixel, y_pixel, largura_pixel, altura_pixel))
pygame.display.flip()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)

pygame.quit()