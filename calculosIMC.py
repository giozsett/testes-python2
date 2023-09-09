

print("Cálculo do IMC")

nome = input("Informe seu nome.")
idade = input("Informe sua idade.")
altura = float(input("Informe sua altura em metros, sem incluir a unidade de medida na resposta (exemplo: 1.64)."))
peso = float(input("Informe seu peso em kg, sem incluir a unidade de medida na resposta (exemplo: 67)."))

print(f"Olá, {nome}.")
print(f"Sua idade é {idade} anos.")
imc = peso / (altura) ** 2
print("Seu IMC é igual a", imc)