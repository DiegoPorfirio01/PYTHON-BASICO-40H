frase = str(input('Qual a frase ? ')).upper().strip()
print ('A LETRA A-a , aparece {} vezes '.format( (frase.count('A'))))
print('A PRIMEIRA LETRA -A- , APARECEU NA POSIÇÃO {} ...'.format(frase.find('A')+1))
print('A ULTIMA NA POSIÇÃO{} ' .format(frase.rfind('A')+1))


