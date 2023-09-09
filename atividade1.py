# Atividade 1 - Operadores Aritméticos e Lógicos

a = 7
b = 2
c = 4
d = 14

print("----------------------")
print("ATIVIDADE 1: OPERAÇÕES")
print("----------------------")
print(".")

print("Primeira operação: A + B - C")
resultado1 = a + b - c
print(f"{a} + {b} - {c} = {resultado1}")
print(".")

print("Segunda operação: A * B / C")
resultado2 = a * b / c
print(f"{a} * {b} / {c} = {resultado2}")
print(".")

print("Terceira operação: C + 22 * D")
resultado3 = c + 22 * d
print(f"{c} + 22 * {d} = {resultado3}")
print(".")

print("Quarta operação: A + B * C + D")
resultado4 = a + b * c + d
print(f"{a} + {b} * {c} + {d} = {resultado4}")
print(".")

print("Quinta operação: (A + B) * (C + D)")
resultado5 = (a + b) * (c + d)
print(f"({a} + {b}) * ({c} + {d}) = {resultado5}")
print(".")

print("Sexta operação: (D / A) / (B / C)")
resultado6 = (d / a) / (b / c)
print(f"({d} / {a}) / ({b} / {c}) = {resultado6}")
print(".")

print("Sétima operação: 10 ** A")
resultado7 = 10 ** a
print(f"10 ** {a} = {resultado7}")
print(".")

print("Oitava operação: 58 % A")
resultado8 = 58 % a
print(f"58 % {a} = {resultado8}")
print(".")

print("Nona operação: (A + B + C * D) / (B - C * (B - C))")
resultado9 = (a + b + c * c) / (b - c * (b - c))
print(f"({a} + {b} + {c} * {d}) / ({b} - {c} * ({b} - {c})) = {resultado9}")
print(".")

print("Décima operação: (A + B + C * D) / (B - C * (B - C)) + 10 ** A")
resultado10 = (a + b + c * d) / (b - c * (b - c)) + 10 ** a
print(f"({a} + {b} + {c} * {d}) / ({b} - {c} * ({b} - {c})) + 10 ** {a} = {resultado10}")
print(".")
