# ADIVINHAÇÃO DE NÚMEROS
# Sistema sorteia 1 número e guarda o número.
# Usuário tenta adivinhar o número.
# Sistema diz se o número está certo ou errado e se o número é > ou < que o palpite.


print("Adivinhação de números de 1 a 100")
print("")

# IMPORTANDO O GERADOR DE NÚMEROS INTEIROS ALEATÓRIOS.
from random import randint
numero_certo = randint(1, 100)


tentativa = int(input("Tente adivinhar o número: "))

while tentativa != numero_certo:
    if tentativa > numero_certo:
        print("O número é <", tentativa)
    elif tentativa < numero_certo:
        print("O número é >", tentativa)
    tentativa = int(input("Tente novamente: "))

if tentativa == numero_certo:
    print("Parabéns, você acertou!")












    



   

