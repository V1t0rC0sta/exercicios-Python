from random import randint
sorteio = int(input('Olá! tente advinhar o número que estou pensando entre 0 e 10: '))
resultado = randint(0, 10)
if sorteio == resultado:
    print(f'O seu número escolhido foi {sorteio} e o meu foi {resultado} também, '
          f'parece que estamos pensando igual hoje!')
else:
    print(f'O seu número escolhido foi {sorteio} e o meu foi {resultado}, '
          f'nossas mentes não estão sicronizadas hoje hehehe.')
print('Aperte o play se quiser uma nova rodada :) ')
