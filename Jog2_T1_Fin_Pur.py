import pandas as pd
import numpy as np

def to_string(x):
    t = '{}'.format(x)
    return t

def JG2_T1_EP_EF(J1E, J2E, menor, maior, partial='jogo'):
    '''
    Parâmetros:
    - J1E: Número de estratégias do jogador 1
    - J2E: Número de estratégias do jogador 2
    - menor: valor mínimo do payoff
    - maior: valor máximo do payoff
    - partial: ['J1', 'J2']
    ''' 
    linhas = list(range(1, J1E+1))
    linhas = ['s_{}'.format(x) for x in linhas]
    
    colunas = list(range(1, J2E+1))
    colunas =['s_{}'.format(x) for x in colunas]
        
    payoff_array1 = np.random.ranf((J1E, J2E))
    payoff_array1 = (maior - menor)*payoff_array1 + menor
    payoff1 = pd.DataFrame(payoff_array1, index = linhas, columns = colunas)
    
    payoff_array2 = np.random.ranf((J1E, J2E))
    payoff_array2 = (maior - menor)*payoff_array2 + menor
    payoff2 = pd.DataFrame(payoff_array2, index = linhas, columns = colunas)
    
    if partial == 'J1':
        representação = payoff1
    
    elif partial == 'J2':
        representação = payoff2
    
    elif partial == 'jogo': 
        payoff = payoff1.round(2).astype(str) +', '+ payoff2.round(2).astype(str)
        representação = pd.DataFrame(payoff, index = linhas, columns = colunas)
        
    else:
        representação = print('Argumento partial inválido. Tente não aplicá-lo ou aplique J1 ou J2')
        
    return representação