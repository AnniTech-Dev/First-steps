print('\033[1;36m SISTEMA DE CONTROLE DE PESO E FRETE\033[m')
print('-==-' * 9)
regis = input('Quer registrar uma caixa? ').upper().strip()
cont = 0
total = 0
total_desc = 0
while regis != 'N':
    kg = int(input('Digite o peso da caixa em kg: '))
    g = kg * 1000
    fre = kg * 5
    print(f'O peso de \033[34m {kg} kg \033[m convertido para g é \033[34m {g} g \033[m')
    print(f'O frete desse produto será \033[34m R${fre:.2f} \033[m')
    caixa = input('A caixa chegou amassada? ').strip().upper()
    if caixa == 'SIM':
        desc = fre * 10 / 100
        print(f'Com o desconto de \033[34m R${desc:.2f} \033[m ficará \033[34m {fre - desc:.2f} \033[m')
        total_desc += desc
    else:
        print('\033[31m Sem desconto.\033[m')
    print('-' * 40)
    regis = input('Quer Registrar mais uma caixa? [S/N]: ').strip().upper()
    print('-' * 40)
    cont += 1
    total += fre
print(f'Voce registrou \033[34m {cont} \033[m caixas.')
print(f'O total bruto foi \033[34m R${total:.2f} \033[m')
print(f'O total liquido foi \033[34m R${total - total_desc:.2f} \033[m')
