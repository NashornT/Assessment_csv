import pandas as pd
import matplotlib.pyplot as pit

arquivo = pd.read_csv('Assessment_PIBs.csv',sep=',')

dados = pd.DataFrame(arquivo)
dados.set_index('País',inplace=True)
# Teste
def solicitador_pib():
    try:
        pais = input('Digite o pais: ').title()
        ano =  int(input('Digite um ano entre 2013 e 2020: '))
        if (ano < 2013 and ano > 2020):
            print('Ano invalido!!')
        else:
            ano = str(ano)
            if (pais == 'Eua'):
                pais = 'EUA'
            elif(pais == 'Coreia Do Sul'):
                pais = 'Coreia do Sul'
            else:
                pass

            print(f'PIB do {pais} em {ano}: U$ {dados.loc[pais][ano]} trilhões.')
    except:
        print('Valor Invalido!!')


def variacoes_anos():
    for i in range(0,15):
            ultimo = dados.iloc[i][7] 
            primeiro = dados.iloc[i][0]

            print(f'{dados.index[i]:<15} Variação de {((ultimo*100)/primeiro)-100:.2f}% entre 2013 e 2020.')

def grafico_pib():
    x = [] 
    y = []
    try:
        pais = input('Digite o pais: ').title()
        if(pais == 'Eua'):
            pais = 'EUA'
        elif(pais == 'Coreia Do Sul'):
            pais = 'Coreia do Sul'

        for i in dados.loc[pais].index:
            x.append(i)
        for i in dados.loc[pais].values:
            y.append(i)

        pit.plot(x,y, label= 'Evolução do PIB')
        pit.xlabel('Anos')
        pit.ylabel('PIB')
        pit.legend()
        pit.show()
    except:
        print('Valor Invalido!!')
    
for i in dados.loc['Brasil'].index:
    pass

solicitador_pib()
print('~~~'*20)
variacoes_anos()
print('~~~'*20)
grafico_pib()