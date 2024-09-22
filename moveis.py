import pygame
import random

pygame.init()

LINE_WIDTH = 1
LINE_WIDTH2 = 2

def draw_furnitures(screen, comodo, moveis):
    if comodo in moveis:
        # Seleciona 3 móveis aleatoriamente do cômodo
        moveis_selecionados = moveis[comodo]

        for movel in moveis_selecionados:
            # Desenha cada móvel na tela
            pygame.draw.rect(screen, movel.cor, (movel.x, movel.y, movel.largura, movel.altura))

class movel:
    def __init__(self, nome, largura, altura, cor, escala, medidas):
        self.nome = nome
        self.largura = round(largura * escala)
        self.altura = round(altura * escala)
        self.cor = cor
        
        # Tenta a posição inicial
        if self.cabe(medidas):
            self.x = random.randint(medidas[0], medidas[0] + medidas[2] - self.largura)
            self.y = random.randint(medidas[1], medidas[1] + medidas[3] - self.altura)
        else:
            # Rotaciona o móvel e tenta novamente
            self.largura, self.altura = self.altura, self.largura  # Inverte largura e altura
            if self.cabe(medidas):
                self.x = random.randint(medidas[0], medidas[0] + medidas[2] - self.largura)
                self.y = random.randint(medidas[1], medidas[1] + medidas[3] - self.altura)
            else:
                raise ValueError(f"O móvel {nome} não cabe no cômodo, mesmo rotacionado.")
    
    def cabe(self, medidas):
        # Verifica se o móvel cabe no cômodo
        # print(medidas)
        return self.largura <= medidas[2] and self.altura <= medidas[3]
    

    def __repr__(self):
        return f"{self.nome}\nlargura: {self.largura}\naltura: {self.altura}\nX: {self.x}\nY: {self.y}"
    

class Porta:
    def __init__(self, x, y, escala):
        self.largura = 0.90 * escala
        self.x = x 
        self.y = y
        self.cor = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.line(screen, self.cor, (self.x, self.y), (self.largura + self.x, self.y), LINE_WIDTH2)

class Janela:
    def __init__(self, x, y, escala):
        self.largura = 1.50 * escala
        self.x = x
        self.y = y 
        self.cor = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.line(screen, self.cor, (self.x, self.y), (self.largura + self.x, self.y), LINE_WIDTH2)
