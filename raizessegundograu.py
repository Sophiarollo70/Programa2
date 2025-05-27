from math import sqrt
A= float(input("Digite o valor de A: "))
B= float(input("Digite o valor de B: "))
C= float(input("Digite o valor de C: "))

if A == 0:
    print("Não pode divisao por 0")
else:
    delta= (B ** 2) - (4 * A * C)
    if delta < 0:
        print("delta invalido - negativo")
    else:
        x1= (-B + sqrt(delta)) / (2 * A)
        x2= (-B - sqrt(delta)) / (2 * A)
        print("Raiz 1:", x1)
        print("Raiz 2:", x2)
