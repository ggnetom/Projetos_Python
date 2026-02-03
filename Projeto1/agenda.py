# IIMPORTANTE
#  esta com bug de quando exporta o arquivo ele nao vai para a pasta que esta o codigo

agenda = {}


def mostrar_contatos():
    if agenda:    
        for contato in agenda:
            buscar_contato(contato)
    else:
        print('A agenda esta vazia')
        print('----------------------------------------')


def buscar_contato(contato):
    try:
        print("nome:", contato)
        print("telefone:", agenda[contato]['tel'])
        print("email:", agenda[contato]['email'])
        print("endereco:", agenda[contato]['endereco'])
        print('----------------------------------------')
    except KeyError:
        print(">>>>>Contato nao existe")
        print('----------------------------------------')
    except:
        print(">>>>>Um erro inesperado ocorreu")
        print('----------------------------------------')

def ler_detalhes_contato():
    tel = input('Digite o telefone:')
    email = input('Digite o email:')
    endereco = input('Digite o nendereco:')
    return tel, email, endereco

def registrar_editar_contato(contato, tel, email, endereco):
    agenda[contato]={
        'tel': tel,
        'email':email,
        'endereco': endereco,
    }
    salvar()
    print('----------------------------------------')


def deletar_contato(contato):
    try:
        agenda.pop(contato)
        salvar()
        print('Contato excluido com sucesso')
        print('----------------------------------------')
    except KeyError:
        print('>>>>>Contato inexistente')
        print('----------------------------------------')
    except:
        print(">>>>>Um erro inesperado ocorreu")
        print('----------------------------------------')


def exportar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in agenda:
                telefone = agenda[contato]['tel']
                email = agenda[contato]['email']
                endereco = agenda[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('>>>>>Agenda exportada!')
        print('----------------------------------------')
    except:
        print('>>>>>Algum erro ocorreu!')
        print('----------------------------------------')


def importar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                registrar_editar_contato(nome, tel, email, endereco)
    except FileNotFoundError:
        print('>>>>>Arquivo nao encontrado!')
        print('----------------------------------------')
    except:
        print('>>>>>Algum erro ocorreu!')
        print('----------------------------------------')

def salvar():
    exportar_agenda('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                agenda[nome]={
                    'tel': tel,
                    'email':email,
                    'endereco': endereco,
                }
        print('>>>>>{} contatos carregados'.format(len(agenda)))
    except FileNotFoundError:
        print('>>>>>Arquivo nao encontrado!')
        print('----------------------------------------')
    except:
        print('>>>>>Algum erro ocorreu!')
        print('----------------------------------------')

def menu():
    print('----------------------------------------')
    print('1 - Mostrar todos contatos')
    print('2 - Buscar conmtato')
    print('3 - Criar contato')
    print('4 - Excluir contato')
    print('5 - Editar Contato')
    print('6 - Exportar contatos para csv')
    print('7 - Importar contatos para csv')
    print('0 - Sair')
    print('----------------------------------------')


carregar()
while True:
    menu()

    opcao = input('Escolha uma opcao: ')
    print('----------------------------------------')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do conatato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            agenda[contato]
            print('este contato ja existe')
            print('----------------------------------------')
        except:
            tel, email, endereco = ler_detalhes_contato()
            registrar_editar_contato(contato, tel, email, endereco)
            print("Contato {} adicionado".format(contato))
    
    elif opcao == '4':
        contato = input('Qual contato quer excluir: ')
        deletar_contato(contato)
    
    elif opcao == '5':
        contato = input('qual contato quer editar: ')
        try:
            agenda[contato]
            buscar_contato(contato)
            tel, email, endereco = ler_detalhes_contato()
            registrar_editar_contato(contato, tel, email, endereco)
            print("Contato {} editado".format(contato))
        except:
            print('Este contato nao existe')
            print('----------------------------------------')

    elif opcao == '6':
        input('Digite o nome do arquivo para ser exportado: ')
        exportar_agenda(nome_do_arquivo)
        print('----------------------------------------')

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        importar_agenda(nome_do_arquivo)
        print('----------------------------------------')

    elif opcao == '0':
        print('>>>>>Saindo')
        print('----------------------------------------')
        break

    else:
        print('Opcao invalida!')
        print('----------------------------------------')