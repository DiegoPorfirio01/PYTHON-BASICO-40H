from random import randint
from time import sleep
computador = randint(0,5)   #faz o PC PENSAR
print( '-=-' *10)
print('vou num numero entre 0 e 5, tente adivinhar....')
print(' PENSANDO .....')
sleep(5)
jogador = int(input('em que numero eu pensei?')) #jogador tenta adivinhar
print('-=-' *10)
if jogador == computador :
    print(' VOCÊ ME VENCEU HUMANO !!')
else:
    print(' VOCÊ PERDEU - SACO DE CARNE . PENSEI NO NUMERO {} !'.format(computador))
