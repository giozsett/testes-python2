# Agora inclui as correções feitas na aula

print("-------------------")
print("CALCULADORA SIMPLES")
print("-------------------")
print(".")
print(".")

num1 = float(input("Qual o primeiro número?"))
num2 = float(input("Qual o segundo número?"))
operacao = input("Escolha uma operação (*, +, -, ou /).")

rMultiplic = num1 * num2
rSoma = num1 + num2
rSubtracao = num1 - num2


if operacao == "*": 
    print(f"{num1} * {num2} = {rMultiplic}")
elif operacao == "+": 
    print(f"{num1} + {num2} = {rSoma}")
elif operacao == "-": 
    print(f"{num1} - {num2} = {rSubtracao}")
elif operacao == "/":
    if num2 != "0":
         resultado = num1 / num2
         print(f"{num1} / {num2} = {resultado}")
    else:
        pass
        print("Não é possível dividir por 0.")
       
else: 
    print("Operação inválida.")