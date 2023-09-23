# CÁLCULO DE MÉDIAS
# Programa deve solicitar o nome dos alunos e suas notas de 4 provas.
# Ao final deve imprimir o nome dos alunos e suas médias.


lista_alunos = []
lista_alunos.append(input("Informe o nome do aluno: "))
primeira_nota = float(input("Informe a nota da 1ª prova: "))
segunda_nota = float(input("Informe a nota da 2ª prova: "))
terceira_nota = float(input("Informe a nota da 3ª prova: "))
quarta_nota = float(input("Informe a nota da 4ª prova: "))
media_alunos = []
media_alunos.append((primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4)
incluir_aluno = input("Deseja incluir mais algum aluno? (s/n) ")


while incluir_aluno == "s":
    lista_alunos = []
    lista_alunos.append(input("Informe o nome do aluno: "))
    primeira_nota = float(input("Informe a nota da 1ª prova: "))
    segunda_nota = float(input("Informe a nota da 2ª prova: "))
    terceira_nota = float(input("Informe a nota da 3ª prova: "))
    quarta_nota = float(input("Informe a nota da 4ª prova: "))
    media_alunos = []
    media_alunos.append((primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4)
    incluir_aluno = input("Deseja incluir mais algum aluno? (s/n) ")

if incluir_aluno == "n":
    print(lista_alunos)
    print(media_alunos)