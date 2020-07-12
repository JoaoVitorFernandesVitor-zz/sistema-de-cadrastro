from os.path import exists
from Funcoes114 import *

#Programa Principal
select = 0

while True:

    if not exists('lista_de_cadastrados.txt'):
        with open('lista_de_cadastrados.txt', 'a+') as file:
            file.write('-' * 50)
            file.write('\n')
            file.write('\033[32mPessoas Cadastradas\033[m'.center(50))
            file.write('\n')
            file.write('-' * 50)

    if select == 0:
       Cena('menu')
       select = leia_num('Sua Opção:',int,True)
    
    # Aba do Menu
    while select == 1:

        with open('lista_de_cadastrados.txt', 'a+') as file:
            file.seek(0)#voltando no inicio do texto
            print(file.read())
            select = 0
    
    # Aba de Novo Cadrastro
    while select == 2:
        try:
            Cena('new')
            nome = leia_text('Digite seu nome:')
            idade = leia_num('Digite sua idade:',int)
            usuario = f'\n{nome}' + f'     {idade}'.center(47)
            with open('lista_de_cadastrados.txt','a+') as file:
                file.write(usuario)
        except:
            print('\033[31mErro no Cadrastro\033[m')

        else:
            title('Cadastrado com sucesso')
        select = 0
    if select == 3:
        Cena('exit')
        break