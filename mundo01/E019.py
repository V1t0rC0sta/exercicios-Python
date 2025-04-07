import random
print('---Sorteio para apagar o quadro---')
a = str(input('Diga o primeiro nome:'))
b = str(input('Diga o segundo nome:'))
c = str(input('Diga o terceiro nome:'))
d = str(input('Por fim, diga um último nome para o sorteio:'))
list = [a, b, c, d]
escolha = random.choice(list)
print(f'O aluno escolhido foi {escolha}')
