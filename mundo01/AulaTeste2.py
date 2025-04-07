v1 = int(input("Digite um valor inteiro:"))
v2 = int(input("Digite um segundo valor inteiro:"))
if v2 < 0:
    print("Não podemos realizar divisõs por 0, vamos tentar mais uma vez.")
else:
    d = v1 / v2
    print(f"{v1} dividido por {v2} é igual a {d}.")
