print('\033[1;34mIMC\033[m')
peso = float(input('Qual o seu peso?(Kg) '))
altura = float(input('Qual a sua altura?(m) '))
imc = peso / (altura ** 2)
print(f'O IMC é: {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA')
