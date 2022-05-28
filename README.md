# Assessment_csv

Questão 3 

    Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, 
    no máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte. 
    Esses valores não devem ser totalmente desprezados, 
    mas não podem funcionar como um norte para o orçamento doméstico de todas as famílias.
    
 Crie um programa contendo uma função que, dados um valor de renda mensal total, 
 gastos totais com moradia, gastos totais com educação e gastos totais com transporte,
 faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, 
 informando qual é o percentual da renda mensal total comprometido por cada custo. 
 
Se o gasto estiver dentro do percentual recomendado, informe ainda que 

Seus gastos estão dentro da margem recomendada.

Caso contrário, informe:


Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
  

Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.

Questão 4

    Osjuros compostos são a força mais poderosa do universo e a maior invenção da humanidade, 
    porque permitem uma confiável e sistemática acumulação de riqueza
A frase, curiosamente, é de Albert Einstein, não de algum banqueiro ou gestor de fundos de capitais. 

Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês.
Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.

No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.

No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.

Ao final de 120 meses, você terá o montante final de R$187.303,05.

Crie um programa que ponha a hipótese de Einstein à prova. 
Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, 
um valor de aporte para cada período e uma quantidade de períodos.


Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e,
no eixo das ordenadas (vertical), o valor acumulado, em reais.


Questão 5

Considere a seguinte projeção de PIBs feita pelo FMI em 2014:

Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020 – ordem decrescente de 2014)*
          (TABELA DENTRO DO ARQUIVO  ASSESSMENT)

(Use a função Arquivo → Fazer o download → csv, para baixar uma versão formatada dos dados para usá-los no projeto)

Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano. 
O programa solicita ao usuário o nome do país e o ano desejado.
Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem: 
País não disponível.

ou

Ano não disponível.

a depender do tipo de dado não encontrado. 


Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual, entre 2013 e 2020.



Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)
