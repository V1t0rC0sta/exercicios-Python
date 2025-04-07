# Leitor de velocidade
vel = int(input('Olá, diga em qual velocidade você esta no momento em Km/h: '))
multa = (vel - 80) * 7
if vel <= 80:
    print(f'Ok, como a sua velocidade é {vel} Km/h , você esta dento do limete de tolerância.')
else:
    print(f'Hummm, infelizmente você esta acima da velocidade permitida. Um momento, pois estamos calculando a sua multa...')
    print(f'Como você estava {vel - 80} Km/h acima da velocidade, a sua multa ficou com o valor de R$ {multa}.')
    print('Tenha mais cuidado!')
