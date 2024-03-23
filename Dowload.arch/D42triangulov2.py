print('Analise de triângulo')
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print(f'Pode se formar um triângulo:')
    if reta1 == reta2 == reta3:
        print('\033[1;31mEQUILATERO')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('\033[1;36mISOCELES')
    elif reta1 != reta2 != reta3 != reta1:
        print('\033[1;33mESCALENO')
else:
    print('NÃO DÁ PARA FORMAR UM TRIÂNGULO')
