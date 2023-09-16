# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, 
# classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

# com as correções feitas na aula

print("----------------------")
print("CLASSIFICAÇÃO DE NOTAS")
print("----------------------")
print(".")
print(".")

nota = float(input("Informe uma nota de 0 a 100:"))

if nota < 60: 
    print(f"{nota} atingiu classificação F.")
elif nota <= 69 and nota >= 60:
    print(f"{nota} atingiu classificação D.")
elif nota <= 79 and nota >= 70:
    print(f"{nota} atingiu classificação C.")
elif nota <= 89 and nota >=80:
    print(f"{nota} atingiu classificação B.")
elif nota <= 100 and nota >= 90:
    print(f"{nota} atingiu classificação A.")
else:
    print("Nota inválida. A nota deve ser de 0 a 100.")
