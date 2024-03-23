print('-=' * 3, 'LOJA', '=-' * 3)
valor = float(input('Valor das compras: R$'))
print('[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    valor1 = (valor * 90) / 100
    print(f'A sua compra à vista fica com 10% de desconto,totalizando R${valor1:.2f}')
elif opçao == 2:
    valor2 = (valor * 95) / 100
    print(f'A sua compra à vista no cartão fica com 5% de desconto,totalizando R${valor2:.2f}')
elif opçao == 3:
    print(f'A sua compra 2x no cartão equivale à R${valor/2:.2f} cada parcela,totalizando R${valor:.2f}')
elif opçao == 4:
    parcela = int(input('Quantas parcelas? '))
    valor4 = valor * (120/100)
    print(f'Sua compra será parcelada em {parcela}x de R${valor4/parcela} COM JUROS')
    print(f'Sua compra de R${valor},vai custar R${valor4} no final.')
else:
    print('INVALIDO')
