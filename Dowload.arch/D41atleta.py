from datetime import date
print('\033[1;34mConfederação Nacional de Natação\033[m')
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(f'Sua idade é {idade}')
if idade <= 9:
    print('Categoria: \033[1;34mMIRIM')
elif 9 < idade <= 14:
    print('Categoria: \033[1;35mINFANTIL')
elif 14 < idade <= 19:
    print('Categoria: \033[1;36mJÚNIOR')
elif 19 < idade <= 25:
    print('Categoria: \033[1;37mSÊNIOR')
elif idade > 25:
    print('Categoria: \033[1;38mMASTER')
