# Uma loja de roupas precisa de um programa que ajude a calcular o valor final da venda de produtos. 
# 1 – A vista – 10% de desconto, se o valor da venda for maior que 500 15%, caso seja maior que 1000, 20% de desconto;
# 2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
# Juros:
# 1 – 11 vezes: 5% de juros ao mês.
# 2 – 12 vezes: 6.5% de juros ao mês.
# 3 – 13 vezes: 7% de juros ao mês.
# 4 – 14 vezes: 9% de juros ao mês.
# 5 – 15 vezes: 9.5% de juros ao mês.
# 6 – 16 vezes: 10% de juros ao mês.
# 7 – 17 vezes: 11.3% de juros ao mês.
# 8 – 18 vezes: 12% de juros ao mês. 

import sys


valor_produtos = float(input("Informe o valor da compra: "))
forma_pagamento = input("Qual a forma de pagamento")

if forma_pagamento == "1":
    valor_final = valor_produtos - valor_produtos * 0.1

    valor_final -= valor_produtos * 0.05 if valor_produtos > 500 else 0
    valor_final -= valor_produtos * 0.05 if valor_produtos > 1000 else 0

# -=   ----> significa: (primeiro valor inserido) - (valor depois do =)

elif forma_pagamento == "2": 
    maxParcela = "18" if valor_produtos > 800 else "5"
    print(f"Você pode parcelar em até {maxParcela} vezes.")
    quantParcela = int(input("Qual o número de parcelas? "))
    
    if (valor_produtos < 800 and quantParcela > 5 and quantParcela > 2):
        print("Quantidade não permitida.")
        sys.exit()
    
    else:
        if (quantParcela > 10):
            if quantParcela == 11: juros = 0.05
            if quantParcela == 12: juros = 0.065
            if quantParcela == 13: juros = 0.07
            if quantParcela == 14: juros = 0.09
            if quantParcela == 15: juros = 0.095
            if quantParcela == 16: juros = 0.1
            if quantParcela == 17: juros = 0.113
            if quantParcela == 18: juros = 0.12
            
            valor_final = valor_produtos + valor_produtos * (juros * quantParcela)
            parcela = (valor_final / quantParcela) * juros

        else: 
            valor_final = valor_produtos
            parcela = valor_final / quantParcela

            # Resumo / Resultados
    if (forma_pagamento == 1):
        print(f"Valor total da compra = {valor_final}")
        print("Total de desconto = " % valor_produtos - valor_final)

    else:
        print("O valor da compra é de %.2f" % valor_final)
        print("Será pago %i de %.2f" %valor_final)

else: print("Forma de pagamento inválida.")

#PROCURAR O CORRIGIDO NO CLASSROOM