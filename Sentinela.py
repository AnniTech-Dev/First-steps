print('======SENTINELA DE FERRO======')
turno = input('DIga o turno do momento: ').strip()
porteiro = input('Nome do porteiro que assumiu o turno: ').strip()
visi = int(input('Quantos visitantes espera receber hoje? '))
menores = 0
maiores = 0
soma = 0
for c in range(1, visi+1):
    nome = input('Nome do visitante: ')
    idade = int(input('Idade do visitante: '))
    soma += idade
    if idade < 18:
        menores = menores + 1
        print('ENTRADA PENDENTE: Aguardar autorização do responsavel.')
    else:
        maiores = maiores + 1
        print('ACESSO LIBERADO: Verifique o documento de identidade.')
media = soma / visi
print('======DADOS DE FIM DE TURNO======')
print(f'O porteiro \033[034m {porteiro}\033[m, trabalhou no turno da \033[034m {turno}.\033[m')
print(f'A quantidade de pessoas que entraram foram \033[034m {visi}\033[m')
print(f'A media de idade é \033[034m {media}\033[m')
print(f'O total de pessoas que foram barradas foram \033[034m {menores}\033[m \n As que foram liberadas foram \033[034m{maiores}\033[m')
print('-=' * 20)
print('TURNO ENCERRADO PELA SENTINELA!')