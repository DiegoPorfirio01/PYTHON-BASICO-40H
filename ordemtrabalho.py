from random import shuffle
a1 = str(input('Qual nome do aluno?'))
a2 = str(input('Qual nome do aluno?'))
a3 = str(input('Qual nome do aluno?'))
a4 = str(input('Qual nome do aluno?'))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('Vão apresentar na ordem : {}'.format(lista))

