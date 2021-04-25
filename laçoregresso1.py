from time import sleep
print('PERDI MINHA MEMÓRIA !! NÃO SEI SE POSSO CONFIAR EM VOCÊ ...')
sleep(2)
resp = str(input('Qual minha cor preferida ?')).strip().lower()
if resp.lower() == "roxa":
    print('HMMMM você me conhece bem....')

else:
    print('VOCÊ NÃO ME CONHECE !')
    sleep(2)
    print('SEU COMPUTADOR IRA SE AUTO DESTRUIR EM:')
    print("-= " *10)
    sleep(2)
    for cont in range(10,0,-1):
        print(cont)
        sleep(1)
    print(" SHUTDOWN ")

