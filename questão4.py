import matplotlib.pyplot as pit


y = []
x = []

def juros():

    try:
        valor_inicial = float(input('Valor inicial: R$ '))
        perc_rendimento = float(input('Rendimento por período:(%) '))
        valor_aport = float(input('Aporte a cada período: R$ '))
        periodos = int(input('Total de períodos: '))


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
            
    except:
        print('Valor Invalido !!')

def grafico():
    juros()
    pit.plot(x,y, label= 'Evolução do valor acumulado')
    pit.xlabel('número de períodos ')
    pit.ylabel('valor acumulado')
    pit.legend()
    pit.show()


grafico()


