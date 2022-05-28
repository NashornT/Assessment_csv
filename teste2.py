'''
def grafico_pib():
    pais = input('Digite o pais: ').title()
    ano = int(input('Selecione o ano: 1 - 2013\n2 - 2014\n3 - 2015\n4 - 2016\n5 - 2017\n6 - 2018\n7 - 2019\n8 - 2020 '))
    if(pais == 'eua'):
        pass
    elif(pais == 'Reino unido'):
        pass
    for i in dic:
        if (dic[i][ano] == '2013' or dic[i][ano] == '2014' or dic[i][ano] == '2015' or dic[i][ano] == '2016' or dic[i][ano] == '2017' or dic[i][ano] == '2018' or dic[i][ano] == '2019' or dic[i][ano] == '2020'):
            pass
        else:
            print(dic[i][ano])
            y.append(float(dic[i][ano]))
            pit.scatter(x,dic[pais])
            pit.show()
'''

def juros(valor_inicial,perc_rendimento,valor_aport,periodos):

    print(f'Valor incial: R$ {valor_inicial}')
    print(f'Rendimento por período:(%){perc_rendimento}')
    print(f'Aporte a cada período: R$ {valor_aport}')
    print(f'Total de períodos: {periodos}')
    

    if(periodos == 0):
        print('Nenhum tempo decorrido')
    else:

        porcen_valor = (valor_inicial*perc_rendimento)/100
        valor = valor_inicial + porcen_valor
        valor_com_aport = valor + valor_aport

        for i in range(1,periodos+1):
             print(f'Após {i} período(s), o montante será de R${valor_com_aport:.2f}.')
             
             y.append(valor_com_aport)
             x.append(i)
             porcen_valor = (valor_com_aport*perc_rendimento)/100
             valor = valor_com_aport + porcen_valor
             valor_com_aport = valor + valor_aport

