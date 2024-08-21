inp = '350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

inp = inp.split()
flag = ""

for i in inp:
    ind = int(i) % 37
    flag += alpha[ind]
print(flag)
