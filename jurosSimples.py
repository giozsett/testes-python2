#Atividade 3

print(".")
print("----------------------------")
print("CALCULADORA DE JUROS SIMPLES")
print("----------------------------")
print(".")
print(".")

vPrincipal = float(input("Informe o valor principal."))
taxaAnual = float(input("Informe a taxa de juros anual."))
tempo = int(input("Informe o período de tempo em anos."))
print(".")

montante = vPrincipal + (vPrincipal * taxaAnual * tempo)
print(f"O montante é igual a {montante} reais no período de {tempo} anos.")
