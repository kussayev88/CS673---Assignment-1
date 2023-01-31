import os

def prit_multiplication_table():
    print('')
    for n in range(1, 13):
        print('{0:6d} * {1:2d} = {2:4d} {3:8d} * {4:2d} = {5:4d} {6:8d} * {7:2d} = {8:4d} {9:8d} * {10:2d} = {11:4d}'.format(i, n, i*n, i+1, n, (i+1)*n, i+2, n, (i+2)*n, i+3, n, (i+3)*n))


print('                                 Multiplication table')

#print valuse for 1 trough 4
i=1
prit_multiplication_table()

#print valuse for 5 trough 8
i=5
prit_multiplication_table()

#print valuse for 9 trough 12
i=9
prit_multiplication_table()

os.system('pause')