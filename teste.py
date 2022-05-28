import matplotlib.pyplot as pit
import numpy as np

'''variação = ((ultimo valor *100)/primeiro valor)-100'''

paises = {
    'EUA':[16.76,17.41,18.12,18.95,19.86,20.76,21.61,22.48],
    'CHINA':[9.46,10.38,11.21,11.96,12.86,13.87,14.96,16.15],
    'JAPÃO':[4.92,4.61,4.21,4.34,4.48,4.59,4.75,4.93],
    'ALEMANHA':[3.73,3.86,3.41,3.51,3.64,3.78,3.93,4.1],
    'REINO UNIDO':[2.68,2.94,2.85,2.98,3.14,3.32,3.51,3.73],
    'FRANÇA':[2.8,2.84,2.47,2.52,2.62,2.73,2.86,3.01],
    'BRASIL':[2.39,2.35,1.9,1.92,2.03,2.13,2.24,2.35],
    'ITÁLIA':[2.13,2.14,1.84,1.88,1.94,2.01,2.08,2.17],
    'ÍNDIA':[1.87,2.05,2.3,2.51,2.75,3.01,3.31,3.64],
    'RÚSSIA':[2.07,2.05,1.17,1.37,1.52,1.69,1.88,2.08],
    'CANADÁ':[1.83,1.78,1.61,1.68,1.76,1.85,1.94,2.04],
    'CORIA DO SUL':[1.3,1.41,1.43,1.51,1.61,1.73,1.86,2.01],
    'ESPANHA':[1.39,1.4,1.23,1.26,1.3,1.35,1.41,1.48],
    'MÉXICO':[1.26,1.28,1.23,1.3,1.37,1.46,1.55,1.65],
    'INDONESIA':[9.13,8.89,8.96,9.52,1.03,1.11,1.2,1.3]

}

anos = [2013,2014,2015,2016,2017,2018,2019,2020]


def solicitador_pib():
    pais = input('Digite o pais: ').upper()
    ano = int(input('Digite um ano entre 2013 e 2020: '))

    if (ano not in anos):
        print('Ano não disponível')
    elif(pais not in paises.keys()):
        print('Pais não disponível')
    else:
        print(f'PIB do {pais} em {ano}: U${paises[pais][anos.index(ano)]} trilhões.')


def variacoes_anos():
    for i in paises:
        print(f'{i :<15} Variação de {((paises[i][7]*100)/paises[i][0])-100:.2f}%')


def grafico_pib():
    pais = input('Digite o pais: ').upper()
    pit.scatter(anos,paises[pais])
    pit.show()


grafico_pib()



