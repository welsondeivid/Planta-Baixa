import pygame
import random

pygame.init()

LINE_WIDTH = 1
LINE_WIDTH2 = 2


def draw_furnitures(screen, comodo, moveis, moveis_usados):

    for chave in moveis:
        if chave.startswith(comodo) or not moveis_usados[chave]:
            print(chave.startswith(comodo), not moveis_usados[chave])
        # Verifica se o nome do cômodo é o início da chave (comodo1, quarto2, etc.)
        if chave.startswith(comodo) and not moveis_usados[chave]:
            print("ENTROU", moveis[chave])
        # Seleciona 3 móveis aleatoriamente do cômodo
            moveis_selecionados = moveis[chave]
            moveis_usados[chave] = True

            print(moveis_selecionados)
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
    def __init__(self, x, y, escala, orientacao):
        if (orientacao == "H"):
            self.largura = 0.90 * escala
            self.altura = None
        else:
            self.altura = 0.90 * escala
            self.largura = None
        self.x = x 
        self.y = y
        self.cor = (0, 0, 255)

    def drawH(self, screen):
        pygame.draw.line(screen, self.cor, (self.x, self.y), (self.largura + self.x, self.y), LINE_WIDTH2)

    def drawV(self, screen):
        pygame.draw.line(screen, self.cor, (self.x, self.y), (self.x, self.altura + self.y), LINE_WIDTH2)

class Janela:
    def __init__(self, x, y, escala, orientacao):
        if (orientacao == "H"):
            self.largura = 1.50 * escala
            self.altura = None
        else:
            self.altura = 1.50 * escala
            self.largura = None
        self.x = x
        self.y = y 
        self.cor = (0, 0, 255)

    def drawH(self, screen):
        pygame.draw.line(screen, self.cor, (self.x, self.y), (self.largura + self.x, self.y), LINE_WIDTH2)

    def drawV(self, screen):
        pygame.draw.line(screen, self.cor, (self.x, self.y), (self.x, self.altura + self.y), LINE_WIDTH2)
