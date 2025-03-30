turmas = int(input("Informe a quantidade de turmas: "))
alunos = int(input("Informe a quantidade total de alunos: "))

media = alunos // turmas

if media > 40:
    print(f"Atencao, media superior a 40 alunos, {media} alunos.")

else:
 print(f"A media de alunos por turma é {media}.")
