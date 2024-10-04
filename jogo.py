import genetico
import menu
import planta_baixa

import pygame

# Captura o input do usuário
menu.menu(pygame)

dados = genetico.main()
print("COORDS", dados.portax, dados.portay)
for andar in dados.andares:
    print("#######################", andar.nome, "#######################")
    print(andar.corridors)
    for comodo in andar.comodos:
        print(f'------{comodo.tipo}')
        print(f'largura: {comodo.largura}, altura: {comodo.altura}')
        print(f'iniciox: {comodo.iniciox}, inicioY: {comodo.inicioy} ')
        print(f'portax: {comodo.portax}, portay: {comodo.portay}')
        print(f'janelax: {comodo.janelax}, janelay: {comodo.janelay}')
        print()
planta_baixa.planta(pygame, dados)
