# TABUADA
# Escreva um código para imprimir a tabuada do 2 usando o laço for.
# Refatore o código para solicitar ao usuário qual tabuada deve ser impressa.

print("")
print("CÁLCULO DA TABUADA")
print("")
print("Feito para calcular os múltiplos de 0 a 10 de um número.")
print("")
print("")

print("Tabuada do número 2:")
# PARTE 1 (tabuada do 2)
for numero2 in range(0, 11):
    print("2 x", numero2, "=", numero2 * 2)


#PARTE 2 (solicita a tabuada)
print("")
numeroEscolhido = int(input("Escolha um número para calcular a tabuada: "))
for numero in range(0, 11):
    print(numeroEscolhido, "x", numero, "=", numeroEscolhido * numero)

    