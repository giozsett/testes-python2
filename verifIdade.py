# Crie um programa que peça ao usuário para inserir sua idade e, em seguida, informe se a pessoa é menor de idade ou maior de idade.

print("--------------------")
print("VERIFICAÇÃO DE IDADE")
print("--------------------")
print(".")

idade = int(input("Informe sua idade:"))
if idade < 18: print("Você é menor de 18 anos.")
else: print("Você é maior de 18 anos.")
  