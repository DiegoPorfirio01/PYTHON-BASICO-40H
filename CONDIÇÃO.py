nome = str(input('Qual seu nome ?')).strip()
n1 = nome.upper()
if n1 == 'DIEGO':
    print('QUE NOME LINDO VOCÊ TEM ')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(n1.title()))