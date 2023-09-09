#Atividade 2

print(".")
print("-----------------------------------")
print("CONVERSOR DE TEMPERATURA")
print("-----------------------------------")
print("De Celsius para Farenheit e Kelvin.")
print("-----------------------------------")
print(".")
print(".")

tcelsius = float(input("Informe a temperatura em graus Celsius (exemplo: 32)."))
print(".")
print(".")

tfarenheit = tcelsius * 1.8 + 32
tkelvin = tcelsius + 273

# Saída
print("Conversão para Farenheit:")
print(f"{tcelsius}°C é igual a {tfarenheit}°F.")
print(".")
print("Conversão para Kelvin:")
print(f"{tcelsius}°C é igual a {tkelvin}.")