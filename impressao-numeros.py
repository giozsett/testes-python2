# EXERCÍCIO
# Usando o for, escrever um programa que imprima números de 1 a 10.
# Refatorar o for para que solicite um número máximo de impressão ao usuário.
# Refatorar o código para que solicite ao usuário se deve ser impresso em ordem crescente ou decrescente.


numero = 0 
for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(numero)


numeroMaximo = int(input("Informe um valor máximo: "))
for numeroMaximo in range(numeroMaximo):
    print(numeroMaximo + 1)



# PARTE 3
numeroMaximo2 = int(input("Informe outro valor máximo: "))
ordem = input("Ordem crescente ou decrescente? (c/d)")

if ordem == "c":
    for numeroMaximo2 in range(1, numeroMaximo2 + 1):
        print(numeroMaximo2)

elif ordem == "d":
    for numeroMaximo2 in range(numeroMaximo2, 0, -1):
        print(numeroMaximo2)

else: 
    print("Ordem inválida.")



    