nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota + nota2) / 2
if media < 5.0:
    print('\033[1;31mREPROVADO\033[m')
    print(f'A sua média foi {media:.1f}')
elif 6.9 > media >= 5.0:
    print('\033[1;36mRECUPERAÇÃO')
    print(f'A sua média foi {media:.1f}')
elif media > 7.0:
    print('\033[1;32mAPROVADO')
    print(f'A sua média foi {media:.1f}')
