import csv
import matplotlib.pyplot as pit


arquivo = open('Assessment_PIBs - modelo 1.csv', 'r',encoding="utf8")
reader = csv.reader(arquivo)
paises = []
anos = []
count = 0
dic = {}
x = []
y = []
razao = 0
pais = []
pib = []


for linha in reader:

    try:
        dic[linha[0]] = linha
    except:
        pass


    for i in linha:
        razao += 1
        if razao == 10:
            paises.append(i)
            razao = 1
        else:
            pass

    if count == 9:
        pass
    else:
        for i in linha:
            count += 1
            if i.isalpha():
                anos.append('') 
            else:
                anos.append(int(i))
                x.append(int(i))  

def solicitador_pib():
    try:
        pais = input('Digite o pais: ').title()
        ano = int(input('Digite um ano entre 2013 e 2020: '))

        if (ano not in anos):
            print('Ano não disponível')
        elif(pais == 'eua'):
            print(f'PIB do {pais} em {ano}: U$ {dic[pais][anos.index(ano)]} trilhões.')
        elif(pais not in paises):
            if (pais == 'Eua'):
                pais = 'EUA'
                print(f'PIB do {pais} em {ano}: U$ {dic[pais][anos.index(ano)]} trilhões.')
            elif(pais == 'Reino unido'):
                pais = 'Reino Unido'
                print(f'PIB do {pais} em {ano}: U$ {dic[pais][anos.index(ano)]} trilhões.')
            elif(pais == 'Coreia Do Sul'):
                pais = 'Coreia do Sul'
                print(f'PIB do {pais} em {ano}: U$ {dic[pais][anos.index(ano)]} trilhões.')
            else:
                print('Pais não disponível')
        else:
            print(f'PIB do {pais} em {ano}: U$ {dic[pais][anos.index(ano)]} trilhões.')
    except:
        print('Valor invalido!!')


def variacoes_anos():
    for i in paises:
        if (i == 'Pais'):
            pass
        else:
            x = float(dic[i][8])
            y = float(dic[i][1])
            print(f'{i :<15} Variação de {((x*100)/y)-100:.2f}% entre 2013 e 2020.')
            

def grafico_pib():
    try:
        pais = input('Digite o pais: ').title()
        if(pais == 'eua' or pais == 'Eua'):
            pais = 'EUA'
        elif(pais == 'Reino unido'):
            pais = 'Reino Unido'
        elif(pais == 'Coreia Do Sul'):
            pais = 'Coreia do Sul'
        for i in dic[pais]:
            if i == pais:
                pass
            else:
                y.append(float(i))

        pit.plot(x,y, label= 'Evolução do PIB')
        pit.xlabel('Anos')
        pit.ylabel('PIB')
        pit.legend()
        pit.show()
    except:
        print('Valor Invalido!! ')        
    
   
  

grafico_pib()



