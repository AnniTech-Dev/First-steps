from time import sleep
#Estrutura de tuplas aninhadas para organizar os dados de forma escalável
feedbacks = (('Adam', 9, 'Resolvido'), ('Julia', 4, 'Pendente'), ('Jonathan', 6, 'Resolvido'),
             ('Amelia', 10, 'Resolvido'), ('Anna', 8, 'Pendente'), ('Larissa', 6, 'Pendente'),('Joao', 3, 'Pendente'), ('Maria', 10, 'Resolvido'), ('Joseph', 5, 'Resolvido'), ('Paulo', 7, 'Pendente'), ('Sophia', 9, 'Pendente'))
nota10 = pend = 0
maior = menor = 9
print(f'{"-" * 43}\n{"RELATÓRIO GERAL":^43}\n{"-" * 43}')
for i, (nome, nota, stts) in enumerate(feedbacks, start=1):
    if nota == 10:
        nota10 += 1
    if stts == 'Pendente':
        print(f'{i}° {(nome):.<25} {nota:_<3} \033[31m{stts}\033[m')
        pend += 1
    else:
        print(f'{i}° {(nome):.<25} {nota:_<3} \033[32m{stts}\033[m')
#Lógica de comparação para identificar os extremos de pontuação
    for nome, nota, stts in feedbacks:
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
print(f'{"-" * 43} \n{"ANÁLISE DE QUALIDADE":^43}\n{"-" * 43}')
print(f'- A maior nota foi \033[34m{maior}\033[m\n- E a menor nota foi \033[34m{menor}\033[m')
print(f'- No total foram \033[34m{nota10}\033[m clientes que deram nota 10')
print(f'- Com status de pendente há \033[34m{pend}\033[m clientes')
print(f'{"-" * 43} \n{"BUSCA":^43}\n{"-" * 43}')
#Loop infinito para permitir multiplas buscas até que o usuário decida sair
while True:
    busca = input('Digite o nome de quem você procura: (S para sair/stop) ').strip()
    if busca.upper() == 'S':
        print('Encerrando a busca...')
        sleep(2)
        break
# Uso de 'Flag' para validar se o nome existe na base de dados
    achou = False
    for nome, nota, stts in feedbacks:
        if busca.capitalize() == nome.capitalize():
            print(f'Achei! {nome} deu a nota {nota}')
            achou = True
            break
    if not achou:
        print('Infelizmente esse cliente não está na lista.\nPor favor tente novamente')