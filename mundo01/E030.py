# Par ou Impar
num = int(input('Olá! Me diga um número inteiro, que eu irei verificar se ele é par ou impar: '))
r = num % 2
if r == 0:
    print(f'O seu número sendo {num}, é um número considerado par.')
else:
    print(f'Por o seu número ser {num}, ele é cosiderado impar.')
