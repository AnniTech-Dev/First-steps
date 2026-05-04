from random import choice
from time import sleep
print(f'{'-' *  53} \n{'GERENCIADOR DE INVENTARIO DE SKINS':^53}\n{'-' * 53}')
# O USUARIO PODE CRIAR OS NOMES DOS ITENS E PESSOAS
itens = list()
nomes = list()
while True:
    obj = input('Escreva o nome do item: (P para parar) ').strip().capitalize()
    if obj == 'P':
        print('Criando a lista de itens...')
        sleep(2)
        break
    itens.append(obj)
print('-' *  45)
while True:
    pess = input('Nome do participante: (P para parar) ').strip().capitalize()
    if pess == 'P':
        print('Criando a lista de participantes...')
        sleep(2)
        break
    nomes.append(pess)
print('-' *  45)
# COLOQUEI EM ORDEM ALFABETICA
nomes.sort()
print('Os nomes em ordem alfabetica:')
for i in nomes:
    print(i)
print('-' * 45)
itens.sort()
print('Os itens em ordem alfabetica:')
for i in itens:
    print(i)
busca = input('Escreva o nome do item que deseja: (C para cancelar) ').strip().capitalize()
# LOOP DE SORTEIO OU NAO
while True: 
    if busca == 'C':
        print('Cancelando...')
        sleep(2)
        break
    if busca in itens:
        sorteio = input('Achamos esse item. Deseja sortea-lo? [S/N] ').strip().upper()
        if sorteio == 'S':
            winner = choice(nomes)
            print('>>>> Voce escolheu sortear o item.')
            sleep(2)
            print(f'>>>> O item sorteado foi {busca} e o(a) ganhador(a) foi {winner}')
            sleep(2)
            # REMOVENDO O ITEM SORTEADO E MOSTRANDO COMO A LISTA FICOU
            itens.remove(busca)
            print('-' * 45)
            print('A lista de itens está assim no momento:')
            for i in itens:
                print(i)
            print('-' * 45)
            busca = input('Continuando...\nEscolha outro item: (C para cancelar) ').strip().capitalize()
        elif sorteio == 'N':
            print('>>>> Voce escolheu não sortear o item.')
            print('-' * 45)
            print('A lista de itens ficou assim:')
            for i in itens:
                print(i)
            print('-' * 45)
            print('Encerrando...')
            sleep(2)
            break
    elif busca not in itens:
        busca = input('Não achamos esse item. tente novamente: (C para cancelar) ').strip().capitalize()
