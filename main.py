import random
import os

bingo = [0] * 75
b = ['--'] * 15
i = ['--'] * 15
n = ['--'] * 15
g = ['--'] * 15
o = ['--'] * 15
ultimas = [''] * 5
#k = 0
#hile k < 75:
#    bingo[k] = k + 1
#    k = k + 1
for k in range(0, 75):
    bingo[k] = k + 1
k = k + 1
while k > 0:
    os.system('clear')
    turno = random.randint(0, k - 1)
    aux = bingo[turno]
    bingo[turno] = bingo[k - 1]
    bingo[k - 1] = aux
    if bingo[k - 1] in range(16):
        bolita = 'B {:2}'.format(bingo[k - 1])
        b[bingo[k - 1] - 1] = '{:2}'.format(bingo[k - 1])
    elif bingo[k - 1] in range(31):
        bolita = 'I {}'.format(bingo[k - 1])
        i[bingo[k - 1] - 16] = '{:2}'.format(bingo[k - 1])
    elif bingo[k - 1] in range(46):
        bolita = 'N {}'.format(bingo[k - 1])
        n[bingo[k - 1] - 31] = '{:2}'.format(bingo[k - 1])
    elif bingo[k - 1] in range(61):
        bolita = 'G {}'.format(bingo[k - 1])
        g[bingo[k - 1] - 46] = '{:2}'.format(bingo[k - 1])
    else:
        bolita = 'O {}'.format(bingo[k - 1])
        o[bingo[k - 1] - 61] = '{:2}'.format(bingo[k - 1])
    print(bolita,'\n')
    for m in range(0, 4):
        ultimas[4 - m] = ultimas[3 - m]
    ultimas[0] = bolita
    print('-'*35,)
    print('Ultimos números que sairam')
    print('{}   {}   {}   {}   {}\n'.format(ultimas[0],ultimas[1],ultimas[2],ultimas[3],ultimas[4],))
    print('-'*35)
    print('{:4}{:4}{:4}{:4}{:4}'.format('B','I','N','G','O'))
    for m in range(0,15):
        print('{:4}{:4}{:4}{:4}{:4}'.format(b[m],i[m],n[m],g[m],o[m]))
    input('')
    k = k - 1
