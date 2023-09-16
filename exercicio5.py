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


print("")
print(" ------------------")
print(" | LOJA DE ROUPAS |")
print(" ------------------")
print("")
print("Programa feito para calcular o valor de pagamento.")
print("")
print("")

valorInicio = float(input("Informe o valor da compra: "))
pagamento = input("Informe o número de parcelas (1 = à vista / >1 = parcelado): ")

if pagamento == 1:
    if valorInicio <= 500:
        valorFinal = valorInicio - 0.1 * valorInicio
        desconto = "10%"
    elif valorInicio <= 1000 and valorInicio > 500:
        valorFinal = valorInicio - 0.15 * valorInicio
        desconto = "15%"
    elif valorInicio > 1000: 
        valorFinal = valorInicio - 0.2 * valorInicio
        desconto = "20%"

    #Saída pagamento à vista:
    print("")
    print("O pagamento será à vista.")
    print(f"O desconto será {desconto}")
    print(f"O valor final da compra será {valorFinal} reais.")

elif pagamento > 0 and pagamento > 1:
    print("É possível parcelar em até 18 vezes.")
    numeroParcelas = int(input("Informe o número de parcelas: "))
    juros = 0
    if numeroParcelas > 0 and numeroParcelas <=18:
        if numeroParcelas <= 10:
            vParcela = valorInicio / numeroParcelas
            valorFinal = valorInicio
        else:
                juros = 5
                vParcela = (valorInicio / numeroParcelas) + (valorInicio / numeroParcelas) * (juros / 100)
                valorFinal = numeroParcelas * vParcela
                if numeroParcelas == 12:
                    juros = juros + 1.5
                elif numeroParcelas == 13:
                    juros = juros + 2
                elif numeroParcelas == 14:
                    juros = juros + 4
                elif numeroParcelas == 15:
                    juros = juros + 4.5
                elif numeroParcelas == 16:
                    juros = juros + 5
                elif numeroParcelas == 17:
                    juros = juros + 6.3
                elif numeroParcelas == 18:
                    juros = juros + 7

        #Saída pagamento parcelado
        print("")
        print(f"O pagamento será parcelado em {numeroParcelas} vezes.")
        print(f"O juros é de {juros}%.")
        print(f"O valor de cada parcela é {vParcela} reais.")
        print(f"O valor final da compra será {valorFinal} reais.")
        
    else:
        print("Número de parcelas inválido.")
else: print("O tipo de pagamento inserido é inválido.")


