from time import sleep
from random import randint

print('=' * 5, 'JOKENPO', '=' * 5)
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogada = int(input('Qual a sua jogada? '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogadapc = randint(0, 2)
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOURA')
sleep(0.5)
print('=' * 30)
print(f'O COMPUTADOR jogou {itens[jogadapc]}')
print('=' * 30)
if jogada == jogadapc:
    print(f'EMPATE,o JOGADOR escolheu {itens[jogada]} e o COMPUTADOR escolheu {itens[jogadapc]}')
elif jogada == 0 and jogadapc == 1:
    print(f'PERDEU,o COMPUTADOR escolheu {itens[jogadapc]}')
elif jogada == 0 and jogadapc == 2:
    print(f'GANHOU,o COMPUTADOR escolheu {itens[jogadapc]} e o JOGADOR escolheu {itens[jogada]}')
elif jogada == 1 and jogadapc == 2:
    print(f'PERDEU,o COMPUTADOR escolheu {itens[jogadapc]}')
elif jogada == 1 and jogadapc == 0:
    print(f'GANHOU,o COMPUTADOR escolheu {itens[jogadapc]} e o JOGADOR escolheu {itens[jogada]}')
elif jogada == 2 and jogadapc == 0:
    print(f'PERDEU,o COMPUTADOR escolheu {itens[jogadapc]}')
elif jogada == 2 and jogadapc == 1:
    print(f'GANHOU,o COMPUTADOR escolheu {itens[jogadapc]} e o JOGADOR escolheu {itens[jogada]}')
else:
    print('INVALIDO')
