v = float(input('Você esta em quantos km/h ?'))
v1 = (v - 80)
v2 = (v1 * 7.0)
if v > 80 :
    print(' VOCÊ ESTA ACIMA DO LIMITE, SUA MULTA É DE {} ! '.format(v2))
else:
    print('PARABENS, VOCÊ É FRACO !')
