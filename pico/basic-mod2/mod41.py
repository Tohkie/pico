inp = '104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42'
alpha = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

inp = inp.split()
flag = ""

for i in inp:
    ind = pow(int(i), -1, 41)
    flag += alpha[ind]
print(flag)
