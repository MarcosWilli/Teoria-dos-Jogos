import pandas as pd
import numpy as np

def estrategias_payoffs(J1E, J2E, menor, maior):
    '''
    Parâmetros:
    - J1E: Número de estratégias do jogador 1
    - J2E: Número de estratégias do jogador 2
    - menor: valor mínimo do payoff
    - maior: valor máximo do payoff
    
    Retorna a representação (DataFrame) dos payoffs de um jogador. A função deve ser chamada duas vezes para obter os dois DataFrames.
    '''
    
    # Criação dos nomes das colunas e das linhas (estratégias):
    linhas = list(range(1, J1E+1))
    linhas = ['s_{}'.format(x) for x in linhas]
    
    colunas = list(range(1, J2E+1))
    colunas =['s_{}'.format(x) for x in colunas]
    
    # Criação do array aleatório com os payoffs de cada jogador
    payoff_array = np.random.ranf((J1E, J2E))
    payoff_array = (maior - menor)*payoff_array + menor
    payoff = pd.DataFrame(payoff_array, index = linhas, columns = colunas).round(2)
    
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
    payoff1: DataFrame contendo os payoffs do jogador 1;
    payoff2: DataFrame contendo os payoffs do jogador 2;
    Obs: 'payoff1' e 'payoff2' devem se referir ao mesmo jogo;
    
    Retorna uma lista contendo os Equilíbrios de Nash do jogo determinado por 'payoff1' e 'payoff2';
    '''
    
    def maximo(payoff, jogador):
        
        # Retorna um objeto que indica a linha ou coluna do maior valor para cada coluna ou cada linha, respectivamente.
        
        maximo = payoff.idxmax(axis=jogador-1)
        maximo = maximo.reset_index()
        maximo = np.array(maximo)
        coluna1 = int((1-(-1)**jogador)/2)
        coluna2 = int((1+(-1)**jogador)/2)
        maximo = maximo[:,coluna1] +', '+ maximo[:,coluna2]
        
        return maximo
    
    solve1 = maximo(payoff1, 1)
    solve2 = maximo(payoff2, 2)
    
    solve = np.intersect1d(solve1, solve2)
    
    return solve

####### Só falta resolver um problema: se existirem valores máximos iguais entre os payoffs, as funções utilizadas pelo pandas e pelo numpy
####### retornam somente a primeira estratégia em vez de retornar todas as estratégias que maximizam o payoff. Fora isso,
####### parece estar correto. Teste no notebook