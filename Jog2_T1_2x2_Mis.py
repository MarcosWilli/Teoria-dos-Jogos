import pandas as pd
import numpy as np
import Jog2_T1_Fin_Pur as jfp

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

def solve(payoff1, payoff2):
    '''
    Parâmetros:
    - payoff1: DataFrame contendo os payoffs do jogador 1;
    - payjoff2: DataFrame contendo os payoffs do jogador 2;
    
    Retorna os Equilíbrios de Nash em estratégias puras e em estratégias mistas
    '''
    
    # Solução em estratégias mistas:
    payoff1 = np.array(payoff1)
    payoff2 = np.array(payoff2)
    
    payoff1_equation = payoff1[0] - payoff1[1]
    payoff1_equation = payoff1_equation.reshape(1,2)
    payoff1_equation = np.concatenate((payoff1_equation, np.array([1,1]).reshape(1,2)), axis = 0)
    resultado1 = np.array([0, 1])
    q = np.linalg.solve(payoff1_equation, resultado1)
    
    payoff2_equation = payoff2[:,0] - payoff2[:,1]
    payoff2_equation = payoff2_equation.reshape(1,2)
    payoff2_equation = np.concatenate((payoff2_equation, np.array([1, 1]).reshape(1,2)), axis = 0)
    resultado2 = np.array([0, 1])
    p = np.linalg.solve(payoff2_equation, resultado2)
    
    pq = np.concatenate((np.array(p).reshape(1,2), np.array(q).reshape(1,2)), axis = 0)
    pq = pd.DataFrame(pq, index = ['Jog 1', 'Jog 2'], columns = ['s_1', 's_2'])
    
    return pq

## Resolver: 

# o código acima está ruim, precisamos melhorálo;

# os resultados podem ser negativos. Logo, temos que colocar uma condição nesse caso, indicando que não há soluções em estratégias mistas.