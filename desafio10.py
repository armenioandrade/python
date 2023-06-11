#ler quanto de dinheiro tem na carteira e calcular quanto em dólares pode-se comprar
#considere U$=1 equivalente a R$3,27

dinheiroNaCarteira = float(input('Quanto de dinheiro vc tem? '))
valorReal = float(3.27)
conversaoEmDolares = dinheiroNaCarteira/valorReal
print('Voce tem R${} que equivale a U${} '.format(valorReal,conversaoEmDolares))