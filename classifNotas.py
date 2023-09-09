# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, 
# classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

print("----------------------")
print("CLASSIFICAÇÃO DE NOTAS")
print("----------------------")
print(".")
print(".")

nota = float(input("Informe uma nota de 0 a 100:"))

if nota >= 90: print(f"{nota} atingiu classificação A.")

# falta terminar