print('Bem vindo a loja Jônatas Abreu')
valorProduto = float(input('Entre com o valor do produto: '))
qtdProduto = int(input('Entre com a quantidade: '))
subTotal = valorProduto * qtdProduto
if qtdProduto < 9:
    valoFinal = subTotal
elif 10 <= qtdProduto < 99:
    valoFinal = subTotal - subTotal * 0.05 #desconto de 5%
elif 100 <= qtdProduto < 999:
    valoFinal = subTotal - subTotal * 0.10 #desconto de 10%
else: # se o valor for acima de 1000 entra nesse else
    valoFinal = subTotal - subTotal * 0.15 #desconto de 15%
print('O valor sem desconto: R$ {:.2f}'.format(subTotal))
print('O Valor com desconto: R$ {:.2f}'.format(valoFinal))