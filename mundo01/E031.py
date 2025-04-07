# Custo de viagem
c = float(input('Olá! Eu sou o cobrador automatico e vou calcular o seu bilhete,'
                'diga a distância a ser percossida em Km: '))
if c <= 200:
    print(f'O valor de passagem calculado é R$ {c*0.50:.2f}')
else:
    print(f'O valor de passagem calculado é de R$ {c*0.45:.2f}')
