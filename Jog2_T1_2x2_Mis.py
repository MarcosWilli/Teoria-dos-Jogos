import pandas as pd
import numpy as np

def estrategias_payoffs(menor, maior):
    '''
    Parâmetros:
    - menor: valor mínimo do payoff
    - maior: valor máximo do payoff
    
    Retorna a representação (DataFrame) dos payoffs de um jogador. A função deve ser chamada duas vezes para obter os dois DataFrames.
    '''
    
    # Criação dos nomes das colunas e das linhas (estratégias):
    linhas_colunas = [1,2]
    linhas_colunas = ['s_{}'.format(x) for x in linhas_colunas]
    
    # Criação do array aleatório com os payoffs de cada jogador
    payoff_array = np.random.ranf((2, 2))
    payoff_array = (maior - menor)*payoff_array + menor
    payoff = pd.DataFrame(payoff_array, index = linhas_colunas, columns = linhas_colunas).round(2)
    
    return payoff

def jogo(payoff1, payoff2):
    '''
    Parâmetros:
    - payoff1: DataFrame contendo os payoffs do jogador 1;
    - payoff2: DataFrame contendo os payoffs do jogador 2;
    
    Retorna a representação do jogo (com 2 jogadores, estratégias puras e finitas e um único período de ação);
    '''
    
    representação = payoff1.astype(str) +', '+ payoff2.astype(str)
        
    return representação