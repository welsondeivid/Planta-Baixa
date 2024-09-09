import pygame
import random

pygame.init()

info = pygame.display.Info()
largura_tela, altura_tela = info.current_w, info.current_h

#Cores dos moveis
SOFA = (255, 0, 0)

AREA_MAX_PIXEL = 1920 * 1080
PIXEL_METRO = 110
LINE_WIDTH = 1

def get_escala():

    with open('input_data.txt', 'r') as file:
        data = file.readline().strip()
        largura_casa, altura_casa = map(int, data.split(' '))

    escala = (largura_casa * altura_casa) / AREA_MAX_PIXEL
    escala_pixel = round(PIXEL_METRO * escala)
    return escala_pixel

def draw_furnitures(screen, comodo, x, y, width, height):
    escala = get_escala()

    if comodo == "livingroom":
        # Calcula o tamanho do sofá com base na escala
        sofa2 = round(0.82 * escala), round(1.72 * escala)

        # Define as posições X e Y para desenhar o sofá dentro dos limites do cômodo
        X = random.randint(x, x + width - sofa2[0])
        Y = random.randint(y, y + height - sofa2[1])

        # Desenha o sofá na tela
        pygame.draw.rect(screen, SOFA, (X, Y, sofa2[0], sofa2[1]))

        print(sofa2[1], y, y + height - sofa2[1])
