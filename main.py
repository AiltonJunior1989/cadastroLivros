def cadastrar_livro(id):
    cadastro = {}
    print('-=' * 10, 'MENU CADASTRAR LIVRO', '-=' * 10)
    cadastro['id'] = id
    cadastro['nome'] = input('Entre com o nome do livro: ')
    cadastro['autor'] = input('Entre com o nome do autor: ')
    cadastro['editora'] = input('Entre com o nome da editora: ')
    return cadastro

def consultar_livro(opcao, lista_livros):
    #print(lista_livros)
    if opcao == 1:
        for l in lista_livros:
            #print(l)
            for k, v in l.items():
                print('{} : {}'.format(k, v))
            print()
    elif opcao == 2:
        id = int(input('Digite o ID do livro: '))
        for l in lista_livros:
            if l['id'] == id:
                for k, v in l.items():
                    print('{} : {}'.format(k, v))
    elif opcao == 3:
        autor = input('Digite o autor do(s) livro(s): ')
        for l in lista_livros:
            if l['autor'] == autor:
                for k, v in l.items():
                    print('{} : {}'.format(k, v))
            print()

def remover_livro(id, lista_livros):
    print(lista_livros)
    i = id - 1
    a = 0
    if lista_livros.pop(i):
        print('Arquivo removido')
        for l in lista_livros:
            l['id'] = a + 1
            a += 1
    else:
        print('Livro não encontrado!')





#Programa principal
print('Bem vindo a Biblioteca do Ailton RU: 4651421')
lista_livro = []
id_global = 0
while True:
    print('-='*10, 'MENU PRINCIPAL', '-='*10)
    print('Escolha a opção desejada;')
    print('1- Cadastrar livro')
    print('2- Consultar livro(s)')
    print('3- Remover livro')
    print('4- Sair')
    sair = int(input('>> '))
    if sair == 1:
        id_global += 1
        lista_livro.append(cadastrar_livro(id_global))
        #print(lista_livro)
        continue
    elif sair == 2:
        while True:
            print('-='*10, 'MENU CONSULTAR LIVRO', '-='*10)
            print('Escolha a opção desejada;')
            print('1- Consultar todos os livros')
            print('2- Consultar livro por ID')
            print('3- Consultar livro(s) por autor')
            print('4- Retomar')
            op = int(input('>> '))
            if op == 4:
                break
            elif op == 1 or op == 2 or op == 3:
                consultar_livro(op, lista_livro)
            else:
                print('Opção inválida!')
                continue
    elif sair == 3:
        print('-=' * 10, 'MENU REMOVER LIVRO', '-=' * 10)
        id = int(input('Digite o ID do livro a ser removido: '))
        remover_livro(id, lista_livro)
        continue
    elif sair == 4:
        print('Finalizando o programa...')
        break
    else:
        print('Opção inválida!')
        continue