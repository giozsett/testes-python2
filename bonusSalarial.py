# Peça ao usuário para inserir seu salário e o tempo de serviço. 
# Se o tempo de serviço  for superior a 5 anos,
# conceda um bônus de 5% ao salário.

# Com as correções feitas na aula.

print("----------------------------- ")
print("| CÁLCULO DO BÔNUS SALARIAL |")
print("----------------------------- ")
print(".")
print(".")

salario = float(input("Informe seu salário: "))
tempo_servico = int(input("Informe o tempo de serviço em anos: "))

if tempo_servico >= 5:
    bonus = 0.05 * salario
    print(f"Você tem direito a um bônus de {bonus} reais.")
else:
    print("Infelizmente você não tem direito ao bônus.")
