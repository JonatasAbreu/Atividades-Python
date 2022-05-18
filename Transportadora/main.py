#----------INICIO DA FUNÇÃO COMPRIMENTO----------
def comprimento():
    while True:
        try:
            compri =float(input('Digitie o comprimento do objeto (em cm):'))
            largura = float(input('Digite a largura do objeto (em cm):'))
            altura = float(input('Digite a altura do objeto (em cm):'))
            print('O volume do objeto é (em cm):{:.2f}'.format(altura * largura * compri))
            if compri < 100:
                return 10.00
            elif compri >= 100 and compri < 10000:
                return 20.00
            elif compri >= 10000 and compri < 30000:
                return 30.00
            elif compri >= 30000 and compri < 100000:
                return 50.00
            else:
                print('Não aceitamos objetos tão pesados\nEntre com dimensões desejadas novamente')
                continue
        except ValueError:
            print('Você digitou alguma dimensão do objeto com o valor não numérico\nPor favor entre com as dimensões desejadas novamente')
            continue
#----------FIM DA FUNÇÃO COMPRIMENTO-------------
#----------INICIO DA FUNÇÃO PESO-----------------
def peso():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg):'))
            if peso <= 0.1:
                return 1
            elif peso >= 0.1 and peso < 1:
                return 1.5
            elif peso >= 1 and peso  < 10:
                return 2
            elif peso >= 10 and peso < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados\nEntre com o peso desejado novamente')
            continue
        except ValueError:
            print('Você digitou o peso do objeto com o valor nâo numérico\nFavor entre com o peso desejado novamente')
#----------FIM DA FUNÇÃO PESO--------------------
#----------INICIO DA FUNÇÃO ROTA-----------------
def rota():
    while True:
        rot = input('Selecione a rota:\nBR - De Brasilia para Rio de Janeiro\nBs - De Brasilia para São Paulo\nRB - De Rio de Janeiro para Brasilia\nRS - De rio de Janeiro para São Paulo\nSR - De São Paulo para Rio de Janeiro\nSB - São Paulo para Brasilia\n')
        if rot == 'RS':
            return 1
        elif rot == 'SR':
            return 1
        elif rot == 'BS':
            return 1.2
        elif rot == 'SB':
            return 1.2
        elif rot == 'BR':
            return 1.5
        elif rot == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe\nPor favor entre com a rota desejada novamente.')
            continue

#------------FIM DA FUNÇÃO ROTA------------------
#-----------MAIN --------------------------------
print('Bem vindo a companhia de logistica Jônatas Abreu(RU:3867774)')
dimensao = comprimento()
peObj = peso()
rotas = rota()
print('Total a pagar(R$): {:.2f}'.format(dimensao * peObj * rotas))

