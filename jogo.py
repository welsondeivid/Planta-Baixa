import genetico
import menu
import planta_baixa

import pygame

# Captura o input do usuário
menu.menu(pygame)

dados = genetico.main()
for andar in dados.andares:
    print("#######################", andar.nome, "#######################")
    for comodo in andar.comodos:
        print(f'------{comodo.tipo}')
        print(f'altura: {comodo.altura}, largura: {comodo.largura}')
        print(f'iniciox: {comodo.iniciox}, inicioY: {comodo.inicioy} ')
        print(f'portax: {comodo.portax}, portay: {comodo.portay}')
        print(f'janelax: {comodo.janelax}, janelay: {comodo.janelay}')
        print()

# ROOMS = {
#         "Térreo": [
#             ["quarto", 100, 300, 4, 3],
#             ["banheiro", 500, 800, 6, 1],
#             ["ginastica", 800, 500, 4, 5]
#         ],
#         "1 Andar": [
#             ["sala", 500, 300, 5, 6],
#             ["cozinha", 900, 800, 4, 3],
#             ["salaDeJantar", 100, 100, 4, 4]
#         ],
#         "Laje": [
#             ["playroom", 100, 300, 6, 5],
#             ["socialbath", 800, 300, 2, 4],
#             ["areaServico", 500, 800, 2, 5]
#         ]
#     }

# print(dados.andares[0].comodos[0].tipo)

planta_baixa.planta(pygame, dados)
