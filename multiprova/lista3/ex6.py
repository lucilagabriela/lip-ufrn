#Um professor está lançando as notas finais da turma de LiP e vendo quem foi aprovado, reprovado ou de recuperação. Você deve escrever um programa para ajudar o professor a determinar a situação de cada aluno com base na nota e no número de faltas do aluno.
# Para ser aprovado, um aluno precisa tirar pelo menos 5 e ter no máximos do que 20 faltas. Uma outra forma de um aluno ser aprovado é se a nota dele for maior ou igual 7.
# Caso o aluno não seja aprovado, se a nota dele for pelo menos 3 e ele tiver no máximo 20 faltas, então pode fazer a recuperação.
# Caso contrário, o aluno está reprovado.
# A nota de um aluno é um número real e o número de faltas é um número inteiro. Cada valor será fornecido em uma linha separada.

nota = float(input(''))
faltas = int(input(''))

if (nota >= 5 and faltas <= 20):
  print('Aprovado')
elif nota >= 7:
  print('Aprovado')
elif nota >= 3 and faltas <= 20:
  print('Recuperação')
else:
  print('Reprovado')