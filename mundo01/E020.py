import random
print('Selecionando pessoas: ')
a = str(input('Diga o nome de um aluno da classe: '))
b = str(input('Diga um segundo nome: '))
c = str(input('Diga um terceiro nome: '))
d = str(input('Diga um quarto nome: '))
lista = [a , b , c , d]
random.shuffle(lista)
print('A ordem esclhida foi : ')
print(lista)
