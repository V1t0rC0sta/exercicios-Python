# teste do exercício
a = int(input('Digite um número de 0 até 9999: '))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print(f'A unidade é = {u}.')
print(f'A dezena é = {d}.')
print(f'A centena é = {c}.')
print(f'O milhar é = {m}.')
