def title(msg):
    print('-' * 50)
    print(f'\033[32m{msg}\033[m')
    print('-' * 50)

def Cena(cena):
    if cena == 'menu':
        title('Menu Principal'.center(50) + '\n'
        '\n1- Ver pessoas cadastradas\n2- Novo Cadastro\n3- Sair do sistema')
    if cena == 'new':
        title('Novo cadastro'.center(50))
    if cena == 'exit':
        title('Sistema Finalizado')


def leia_num(msg,tipo,menu=False):
    #inserir tipos de dados usados no programa
    if tipo == float:
        t = 'real'
    if tipo == int:
        t = ' inteiro'

    while True:
        try:
            x = tipo(input(msg).replace(',','.'));

        except(ValueError, TypeError):
            print(f'\033[31mErro!Digite um numero {t} valido.\033[m')

        if menu:
            if x <= 3 and x >= 0:
                return x
            else:
                print('\033[31mEntrada invalida!\033[m')
        else:
            return x

def leia_text(msg):
    while True:
        x = input(msg)
        if x.isalpha():
            return x
        else:
            print('\033[31mErro!Digite Somente letras\033[m')

