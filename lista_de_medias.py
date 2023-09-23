# CÁLCULO DE MÉDIAS
# Programa deve solicitar o nome dos alunos e suas notas de 4 provas.
# Ao final deve imprimir o nome dos alunos e suas médias.

quantidade_alunos = 1
nome_alunos = []
media_alunos = []
incluir_aluno = "s"


while incluir_aluno == "s":
    quantidade_alunos = quantidade_alunos + 1 
    nome_alunos.append(input("Informe o nome do aluno: "))
    primeira_nota = float(input("Informe a nota da 1ª prova: "))
    segunda_nota = float(input("Informe a nota da 2ª prova: "))
    terceira_nota = float(input("Informe a nota da 3ª prova: "))
    quarta_nota = float(input("Informe a nota da 4ª prova: "))
    media_alunos.append((primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4)
    incluir_aluno = input("Deseja incluir mais algum aluno? (s/n) ")

if incluir_aluno == "n":
    for quantidade_alunos in range(quantidade_alunos):
        print(nome_alunos)
        print(media_alunos)