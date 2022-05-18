acumulador = 0
print(' Bem-Vindo a Lanchonete do Jônatas Abreu (RU:3867774)')
print('******************Cardápio*****************')
print('| Código  |        Descrição      | Valor(R$) |')
print('|   100   |    Cachorro-Quente    |    9,00   |')
print('|   101   | Cachorro-Quente Duplo |    11,00  |')
print('|   102   |          X-Egg        |    12,00  |')
print('|   103   |         X-Salada      |    12,00  |')
print('|   104   |         X-Banco       |    14,00  |')
print('|   104   |          X-Tudo       |    17,00  |')
print('|   104   |  Refrigerante Lata    |     5,00  |')
print('|   104   |     Chá Gelado        |     4,00  |')
while True:
    codigo = input('Entre com o código desejado:')
    if codigo == "100":
        acumulador = acumulador + 9
        print('Voce pediu um Cachorro-Quente no valor de 9,00')
    elif codigo == "101":
        acumulador = acumulador + 11
        print('Voce pediu um Cachorro-Quente Duplo no valor de 11,00')
    elif codigo == "102":
        acumulador = acumulador + 12
        print('Voce pediu um X-Egg no valor de 12,00')
    elif codigo == "103":
        acumulador = acumulador + 12
        print('Voce pediu um X-Salada no valor de 12,00')
    elif codigo == "104":
        acumulador = acumulador + 14
        print('Voce pediu um X-Bacon no valor de 14,00')
    elif codigo == "105":
        acumulador = acumulador + 17
        print('Voce pediu um X-Tudo no valor de 17,00')
    elif codigo == "200":
        acumulador = acumulador + 5
        print('Voce pediu um Refrigerante Lata no valor de 5,00')
    elif codigo == "201":
        acumulador = acumulador + 4
        print('Voce pediu um Chá Gelado no valor de 4,00')
    else:
        print('Opção Inválida')
        continue
    resposta = input('Deseja perdir mais alguma coisa? \n 1 - Sim \n 0 - Não \n')

    if resposta == "1":
        continue
    else:
        print('O total a ser pago é: {:.2f}.'.format(acumulador))
        break

