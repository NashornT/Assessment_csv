def saude_financeira():

    try:
        valor_max = float(input('Digite sua renda mensal: '))
        moradia = float(input('Digite o valor total gasto com moradia: '))
        educacao = float(input('Digite o valor total gasto com educacão: '))
        transporte = float(input('Digite o valor total gasto com transportes: '))



        '''Valor recomendado'''    

        recomendado_moradia = (valor_max*30)/100
        recomendado_educacao = (valor_max*20)/100
        recomendado_transporte = (valor_max*15)/100

        '''Taxas'''

        taxa_moradia = (100*moradia/valor_max)
        taxa_educacao = (100*educacao/valor_max)
        taxa_transporte = (100*transporte/valor_max)


        print('~~~'*20)
        print(f'Renda mensal total: R$ {valor_max}')
        print(f'Gastos totais com moradia: R$ {moradia}')
        print(f'Gastos totais com educação: R$ {educacao}')
        print(f'Gastos totais com transporte: R$ {transporte}')
        print('~~~'*20)




        if(moradia > recomendado_moradia):
            print(f'Seus gastos totais com moradia comprometem {taxa_moradia:.2f}% de sua renda total.\n O máximo recomendado é de 30% . Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${recomendado_moradia:.2f}.')
            print('~~~'*30)
        else:
            print(f'Seus gastos totais com transporte comprometem {taxa_moradia:.2f}% de sua renda total.\n O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.')
            print('~~~'*30)

        if(educacao > recomendado_educacao):
            print(f'Seus gastos totais com educação comprometem {taxa_educacao:.2f}% de sua renda total.\n O máximo recomendado é de 20% . Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${recomendado_educacao:.2f}.')
            print('~~~'*30)
        else:
            print(f'Seus gastos totais com educação comprometem {taxa_educacao:.2f}% de sua renda total.\n O máximo recomendado é de 20% . Portanto, idealmente, Seus gastos estão dentro da margem recomendada. ')
            print('~~~'*30)

        if(transporte > recomendado_transporte):
            print(f'Seus gastos totais com transporte comprometem {taxa_transporte:.2f}% de sua renda total.\n O máximo recomendado é de 15% . Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${recomendado_transporte:.2f}.')
        else:
            print(f'Seus gastos totais com transporte comprometem {taxa_transporte:.2f}% de sua renda total.\n O máximo recomendado é de 15% . Portanto, idealmente, Seus gastos estão dentro da margem recomendada. ')

    except:
        print('Valor valido!!')

saude_financeira()
