def escolher_moveis(moveis, rooms, comodo, escala):
            while not posicao_valida_flag:
                # Cria uma nova instância do móvel com posição aleatória
                novo_movel = mv.movel(movel.nome, movel.largura/escala, movel.altura/escala, movel.cor, escala, medidas)
                
                # Verifica se a posição é válida
                if not posicao_valida(novo_movel, moveis_selecionados, medidas):
                    # Tenta rotacionar o móvel (troca largura e altura)
                    novo_movel = mv.movel(movel.nome, movel.altura/escala, movel.largura/escala, movel.cor, escala, medidas)
                
                # Se ainda não couber, tenta uma nova posição aleatória
                if not posicao_valida(novo_movel, moveis_selecionados, medidas):
                    novo_movel.x = random_posicao_x()  # Gera nova posição X aleatória
                    novo_movel.y = random_posicao_y()  # Gera nova posição Y aleatória
                
                # Verifica se a nova posição/rotação é válida
                posicao_valida_flag = posicao_valida(novo_movel, moveis_selecionados, medidas)
            
            moveis_selecionados.append(novo_movel)
        
        return moveis_selecionados
    return []

def escolher_moveis(moveis, rooms, comodo, escala):
            while not posicao_valida_flag:
                # Cria uma nova instância do móvel com posição aleatória
                novo_movel = mv.movel(movel.nome, movel.largura/escala, movel.altura/escala, movel.cor, escala, medidas)
                posicao_valida_flag = posicao_valida(novo_movel, moveis_selecionados, medidas)
            
            moveis_selecionados.append(novo_movel)
        
        return moveis_selecionados
    return []