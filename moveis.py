import pygame
import random
import sys

pygame.init()

LINE_WIDTH = 1

def draw_furnitures(screen, comodo, moveis):
    if comodo in moveis:
        # Seleciona 3 móveis aleatoriamente do cômodo
        moveis_selecionados = moveis[comodo]

        for movel in moveis_selecionados:
            # Desenha cada móvel na tela
            pygame.draw.rect(screen, movel.cor, (movel.x, movel.y, movel.largura, movel.altura))

class movel:
    def __init__(self, nome, largura, altura, cor, escala, medidas):
        self.cor = cor
        self.nome = nome
        self.largura = round(largura * escala)
        self.altura = round(altura * escala)

        # Gera uma posição aleatória dentro dos limites do cômodo
        self.x = random.randint(medidas[0], medidas[0] + medidas[2] - self.largura)
        self.y = random.randint(medidas[1], medidas[1] + medidas[3] - self.altura)

    def __repr__(self):
        return f"{self.nome}\nlargura: {self.largura}\naltura: {self.altura}\nX: {self.x}\nY: {self.y}"