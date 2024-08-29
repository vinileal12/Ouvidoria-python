
from operacoesbd import *


con = criarConexao('localhost','root','1234','ouvidoria3') #conexão com o banco de dados

opcao = -1
tiposManifestacoes = ['Elogio','Sugestão','Reclamação','Denúncia']

while opcao !=7:

    print('Seja bem vindo à ouvidoria')

    try:
        opcao = int(input("\n1-Listagem das Manifestação.\n2-Listagem de Manifestações por Tipo.\n3-Criar uma nova Manifestação.\n4-Exibir quantidade de manifestações.\n5-Pesquisar uma manifestação por código.\n6-Excluir uma Manifestação pelo Código.\n7-Sair do sistema.\nDigite a opção que deseja: "))
    except:
        print("\nEsse campo so aceita numeros inteiros (1-7)!!\n")
        continue
    print("\nOpção lida", opcao)


    if opcao == 1:


        print('\n===Lista manifestações ===')

        listaSql = 'SELECT * FROM manifestacao'
        resultado = listarBancoDados(con,listaSql)

        if not resultado:
            print('Nao existem manifestações')
        else:
            for item in resultado:
                print(f'\ncodigo:{item[0]}\nDecrição:{item[1]}\ntipo:{item[2]}')


    elif opcao == 2:
        print('\n==LISTAGEM DE MANIFESTÇÃO POR TIPO==')

        for index,item in enumerate(tiposManifestacoes,start=1):
                print(f'{index}-{item}')

        try:
            tipo = int(input('Selecione um tipo:'))
        except:
            print("\nEsse campo so aceita numeros inteiros!!\n")
            continue


        tiposelcionado = tiposManifestacoes[tipo -1]
        selectManiSql = f"SELECT * FROM manifestacao WHERE TIPO ='{tiposelcionado}'"
        resultado = listarBancoDados(con,selectManiSql)


        if not resultado:
            print('Não existem manifestações')
        else:
            for item in resultado:
                print(f'codigo:{item[0]}\nDecrição:{item[1]}\ntipo:{item[2]}')


    elif opcao == 3:

        print('\n====Cria um nova manifestação====')
        for index,item in enumerate(tiposManifestacoes,start=1):
            print(f'{index}-{item}')

        try:
            opcaoselecionada = int(input('digite um opção:'))
            
        except:
            print("\nEsse campo so aceita numeros inteiros!!\n")
            continue

        tipoSelecionado = tiposManifestacoes[opcaoselecionada - 1]

        descricao = input("descreva sua manifestação: ").strip()

        if not descricao:
            print('\nDigite uma mensagem válida!!\n')
        else:

            manifestacao = 'INSERT INTO manifestacao(descricao,tipo) values(%s,%s)'
            dados = [descricao,tipoSelecionado]

            insertNoBancoDados(con,manifestacao,dados)
            print("Manifestação adicionada com sucesso!!!\n")

    elif opcao == 4:

        print('\n~~~~~~~~Exibir quantidade de manifestações~~~~~~~~~~~~\n')

        quantidadeSql = 'SELECT COUNT(*) FROM manifestacao'
        resultado = listarBancoDados(con,quantidadeSql)

        print('Quantidade de manifestação: ',resultado[0][0])


    elif opcao == 5:


        print('\n~~~~~~~~~Pesquisar uma manifestação por código~~~~~~~~~~~\n')
        try:
            pesquisarManifestacao = int(input('Digite o id da manifestação: ')) 
        except:
            print("\nEsse campo so aceita numeros inteiros!!\n")
            continue

        listaSql = f"SELECT * FROM manifestacao WHERE ID ='{pesquisarManifestacao}'"
        resultado = listarBancoDados(con,listaSql)

        if not resultado:
            print('Nao existem manifestações')
        else:
            for item in resultado:
                print(f'codigo:{item[0]}\nDecrição:{item[1]}\ntipo:{item[2]}')

    elif opcao == 6:

        print('\n~~~~~~~~Excluir uma Manifestação pelo Código~~~~~~~~~~~~\n')
        try:
            deletarId = int(input("Digite o ID da manifestação que deseja apagar: "))
        except:
            print("\nEsse campo so aceita numeros inteiros !!\n")
            continue

        apagarSql = f'DELETE FROM manifestacao WHERE ID = (3)'
        dados = [deletarId]

        excluirBancoDados(con,apagarSql,dados)
        print('Manifestação apagada com sucesso!!')

    elif opcao != 7:
        print('\n~~~~~~~~~~~~~~~~~~~~\n')
        print('Opção invalida')


print('Obrigado por usar o sistema!')

encerrarBancoDados(con)
