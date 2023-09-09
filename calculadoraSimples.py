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
rDivisao = num1 / num2

if operacao == "*": print(f"{num1} * {num2} = {rMultiplic}")
if operacao == "+": print(f"{num1} + {num2} = {rSoma}")
if operacao == "-": print(f"{num1} - {num2} = {rSubtracao}")
if operacao == "/": print(f"{num1} / {num2} = {rDivisao}")
else: print("Operação inválida.")