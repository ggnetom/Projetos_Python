filmes = {}
albuns = {}

def ler_filme():
    nota = input("Nota: ")
    comentario = input("Comentario: ")
    return nota, comentario


def mostrar_filmes():
    if filmes:
        for nome_filme in filmes:
            buscar_filme(nome_filme)
    else:
        input('Nao foi registrado nenhum filme')


def mostrar_filme():
    print('Filme: ', nome_filme)
    print('Nota: ', nota)
    print('Comentario: ', comentario)


def buscar_filme(nome_filme):
    try:
        print('Filme: ', nome_filme)
        print('Nota: ', filmes[nome_filme]['nota'])
        print('Comentario: ',filmes[nome_filme]['comentario'])
        print('-------------------------------------')
    except Exception as e:
        print(e)
        print('Filme nao registrado')
        print('-------------------------------------')


def adicionar_filme(nome_filme, nota, comentario):
    filmes[nome_filme]={
        'nota': nota,
        'comentario': comentario
    }
    salvar_filmes()
    print('---------------------------')


def excluir_filme(nome_filme):
    try:
        filmes.pop(nome_filme)
        salvar_filmes()
        print('Filme excluido com sucesso')
        print('---------------------------')
    except:
        print('Filme nao registrado')
        print('---------------------------')


def exportar_filmes(arquivo_filmes):
    try:
        with open(arquivo_filmes, 'w') as arquivo:
            for nome_filme in filmes:
                nota = filmes[nome_filme]['nota']
                comentario = filmes[nome_filme]['comentario']
                arquivo.write('{}, {}, {}\n'.format(nome_filme, nota, comentario))
        print('Filmes Exportados')
        print('---------------------------')
    except:
        print('Algo deu errado')
        print('---------------------------')


def salvar_filmes():
    exportar_filmes('filmes.csv')


def carregar_filmes():
    try:
        with open ('filmes.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))
                nome_filme = detalhes[0]
                nota = detalhes[1]
                comentario = detalhes[2]
                filmes[nome_filme]={
                    'nota': nota,
                    'comentario': comentario
                }
        print('{} filmes carregados'.format(len(filmes)))
        print('---------------------------')
    except FileExistsError:
        print('Arquivo não encontrado')
        print('---------------------------')
    except Exception as e:
        print(e)
        print('Algo deu errado')
        print('---------------------------')


def menu_filme():
    print('1- Adicionar Filme')
    print('2- Buscar Filme')
    print('3- Mostrar todos Filmes')
    print('4- Excluir Filme')
    print('5- SAIR')
    print('---------------------------')


carregar_filmes()
while True:
    menu_filme()
    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        print('---------------------------')
        print('Adicionando Filme')
        nome_filme = input('Filme: ')
        try:
            filmes[nome_filme]
            print('Este filme ja foi adicionado')
            print('---------------------------')
        except:
            nota, comentario = ler_filme()
            adicionar_filme(nome_filme, nota, comentario)
            print('Filme adicionado com sucesso')
            print('---------------------------')
    
    elif opcao == '2':
        print('---------------------------')
        print('Buscando Filme')
        nome_filme = input('Filme: ')
        buscar_filme(nome_filme)
    
    elif opcao == '3':
        print('---------------------------')
        print('Mostrando Filmes')
        mostrar_filmes()

    elif opcao == '4':
        print('---------------------------')
        print('Excluindo Filme')
        nome_filme = input('Filme: ')
        excluir_filme(nome_filme)

    elif opcao == '5':
        print('---------------------------')
        print('SAINDO')
        break

    else:
        print('Opcao Invalida')
