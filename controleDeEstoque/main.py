listaPecas = []

#---------- COMEÇO CadastraPeca ------------
def cadastrarPecas(codigo):
    print('Você selecionou a opção cadastrar peça')
    print('Código da Peça : {}'.format(codigo))
    nome = input('Por favor entre com o NOME da peça: ')
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')
    valor = int(input('Por favor entre com o VALOR(R$) da peça:'))
    dicionarioPecas = {'codigo': codigo,
                           'nome': nome,
                           'fabricante':fabricante,
                           'valor': valor}
    listaPecas.append(dicionarioPecas.copy())
#---------- Fim CasdastrarPeca-------------
#---------- COMEÇO ConsultarPeca ----------
def consultarPeca():
    while True:
        try:
            print('Você selecionou a opção Consultar Peças')
            opConsultar = int(input('Escolha a opção desejada\n'
                                    '1 - consultar Todos as Peças\n'
                                    '2 - Consultar Peças pr Código\n'
                                    '3 - Consultar Peças por Fabricante\n'
                                    '4 - Retornar'))
            if opConsultar == 1:
                for pecas in listaPecas:
                    for key, value in pecas.items():
                        print('{} : {}'.format(key, value))
            elif opConsultar == 2:
                entrada = int(input('Digie o CÓDIGO da Peça:'))
                for pecas in listaPecas:
                    if(pecas['codigo'] == entrada):
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                entrada = input('Digie o FABRICANTE da Peça:')
                for pecas in listaPecas:
                    if (pecas['fabricante'] == entrada):
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                return
            else:
                print('Opção não encontrada')

        except ValueError:
            print('Pare de digitar valores não inteiros')
#---------- Fim ConsultarPeca-------------
#---------- COMEÇO removerPeca ----------
def removerPeca():
    entrada = int(input('Digie o CÓDIGO da peça a ser removida:'))
    for pecas in listaPecas:
        if (pecas['codigo'] == entrada):
            listaPecas.remove(pecas)

#---------- Fim removerPeca-------------
#---------- COMEÇO MAIN ----------
print('Bem-vindo ao Controle do Estoque de Bicicletaria do Jônatas Abreu (RU:3867774')
registroPecas = 0
while True:
    try:
        opcao= int(input('Escolha a opção desejada:\n1 - Cadastrar Peças\n'
                         '2 - Consultar Peças\n'
                         '3 - Remover Peças\n'
                         '4 - Sair'
                         '\n>>'))
        if opcao == 1:
            registroPecas = registroPecas + 1
            cadastrarPecas(registroPecas)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Programa finalizado')
            break
        else:
            print('Opção não encontrada')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros')
#---------- Fim MAIN-------------
