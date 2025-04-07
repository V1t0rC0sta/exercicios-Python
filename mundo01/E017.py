from math import sqrt
print('Calculando a hipotenusa.')
ca = float(input('Informe o valor do cateto adjacente:'))
co = float(input('Informe o valor do cateto oposto:'))
hip = sqrt((ca**2)+(co**2))
print(f'Sendo o cateto adjacente {ca:.2f} e o cateto oposto {co:.2f}, a hipotenusa calculada tem o valor de {hip:.2f}.')
