import pygame
import random

pygame.init()

LINE_WIDTH = 1
LINE_WIDTH2 = 5

def draw_furnitures(screen, comodo, andar, moveis_escolhidos):
    # Percorre a lista de móveis escolhidos, independentemente do nome do cômodo
    for comodo_movel in moveis_escolhidos:
        comodo_id = comodo_movel[0]  # ID do cômodo
          # Lista de móveis para esse cômodo

        # print("comodo: ", comodo, "ANDAR: ", andar, "MOVEIS", comodo_movel)
        # print(comodo_movel[0].split('_'))

        # Para cada móvel na lista de móveis selecionados, desenha o móvel na tela
        check = comodo_id.split('_')
        if check[0] == andar and check[1] == comodo:
            moveis_selecionados = comodo_movel[1]
            print(comodo_id)
            for movel in moveis_selecionados:
                # Desenha o móvel na tela usando pygame
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
        return self.largura <= medidas[2] and self.altura <= medidas[3]
    

    def __repr__(self):
        return f"{self.nome}\nlargura: {self.largura}\naltura: {self.altura}\nX: {self.x}\nY: {self.y}\ncor: {self.cor}"
    

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
